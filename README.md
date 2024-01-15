# Coursera Automatizācija

Python skripts, kas izmanto Selenium un Openpyxl bibliotēkas, lai apkopotu informāciju par kursiem Coursera platformā un saglabātu to Excel failā.

## Projekta Uzdevums
Skripts ir izstrādāts, lai ļautu lietotājiem iegūt informāciju par Coursera kursiem, tos filtrējot pēc dažādiem kritērijiem, piemēram, kursa līmenis, kursa tips un minimālais reitings. Galvenais uzdevums ir izveidot filtrētu kursu sarakstu, kas atbilst lietotāja izvēlētajiem kritērijiem.

## Izmantotas Python bibliotēkas
- **Selenium:** Izmantots, lai automatizētu pārlūka darbības un iegūtu informāciju no Coursera mājaslapas.
- **Openpyxl:** Ļauj izveidot un rediģēt Excel failus, kur tiek saglabāta informācija par kursiem.

## Programmatūras lietošana
1. Lietotājiem tiek piedāvāts ievadīt studiju jomu (piemēram, "JavaScript", "Python").
2. Lietotājiem tiek uzdots jautājums par viņu prasmju līmeni (Beginner, Intermediate, Advanced, Mixed).
3. Lietotājiem tiek uzdots jautājums par minimālo kursa reitingu.
4. Lietotājiem tiek uzdots jautājums par kursa tipu ("Course", "Specialization", "Professional Certificate")

Ievadītā informācija tiek izmantota, lai filtrētu un iegūtu datus par Coursera kursiem, ieskaitot nosaukumu, veidotāju, prasmes, vērtējumu, atsauksmes, līmeni, tipu un ilgumu.

Iegūtie dati tiek saglabāti Excel failā ar nosaukumu "coursera_{ievadītā_studiju_joma}.xlsx."

## Video Demonstrācija
Video demonstrācija parāda skripta darbību, ievades procesu un rezultējošos datus, kas saglabāti Excel failā.
https://www.veed.io/view/93472029-0015-4fa4-8ffb-6db45b8ede2c?panel=share

## Programmas rezultāts
<img width="821" alt="Screenshot 2024-01-15 at 18 28 01" src="https://github.com/nikitahessde/coursera-automation/assets/147872593/44698771-74d4-4cbf-8c5b-097a0767a315">

## Autors
- Nikita Hess 14 grupa

