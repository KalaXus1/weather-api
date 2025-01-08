from csv import DictReader

with open('meteo.csv', encoding='utf-8') as f:
    reponse = DictReader(f)
    meteo = {int(code['Code temps']): code['Description'] for code in reponse}
