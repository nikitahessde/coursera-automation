from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl


def getValidInput(message, valid_options=None):
    while True:
        user_input = input(message)
        try:
            user_input = user_input
            if valid_options is None or user_input in valid_options:
                return user_input
            else:
                print(f"Invalid input. Please choose from {valid_options}")
        except ValueError:
            print("Invalid input. Please enter a valid value.")


course_field = input("Enter field: ")

valid_levels = ["Beginner", "Intermediate", "Advanced", "Mixed"]
your_level = getValidInput("Enter your level (Beginner, Intermediate, Advanced, Mixed): ", valid_levels)

min_rating = getValidInput("Enter the minimal rating of the course (ex. 4.8): ")

valid_types = ["Course", "Specialization", "Professional Certificate"]
required_type = getValidInput("Enter the type of course (Course, Specialization, Professional Certificate): ", valid_types)


workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(['Course Title', 'Course Creator', 'Skills', 'Rating', 'Reviews', 'Level', 'Type', 'Duration'])

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = 'https://www.coursera.org/'
driver.get(url)

find=driver.find_element(By.ID, 'onetrust-accept-btn-handler')
find.click()

find=driver.find_element(By.CLASS_NAME, 'react-autosuggest__input')
find.send_keys(course_field)
find.send_keys(Keys.ENTER)
time.sleep(2)

course_cards = driver.find_elements(By.CLASS_NAME, 'cds-CommonCard-titleLink')
course_creators = driver.find_elements(By.CLASS_NAME, 'cds-ProductCard-partnerInfo')
course_bodies = driver.find_elements(By.CLASS_NAME, 'cds-ProductCard-body')
course_stats = driver.find_elements(By.CLASS_NAME, 'cds-CommonCard-ratings')
course_level_duration = driver.find_elements(By.CLASS_NAME, 'cds-CommonCard-metadata')


for card, creator, body, rating, level_duration in zip(course_cards, course_creators, course_bodies, course_stats, course_level_duration):
    course_title = card.text
    course_creator = creator.text
    course_skills = body.text
    course_rating = rating.text
    course_lev_dur = level_duration.text

    rating_and_reviews = course_rating.split('(')
    course_rating_value = rating_and_reviews[0]
    course_reviews = ''.join(rating_and_reviews[1:]).rstrip(')')
    level_type_duration = course_lev_dur.split(' · ')
    course_level = level_type_duration[0]
    course_type = level_type_duration[1]
    course_duration = level_type_duration[2]

    if course_creator != 'Coursera Project Network':
        if course_level == your_level:
            if float(course_rating_value) >= float(min_rating):
                if course_type == required_type:
                    worksheet.append([course_title, course_creator, course_skills, course_rating_value, course_reviews, course_level, course_type, course_duration])

workbook.save(f'coursera_{course_field}.xlsx')
driver.quit()






