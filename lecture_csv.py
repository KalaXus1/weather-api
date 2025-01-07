
from csv import DictReader
    
with open('meteo.csv') as f:
    reponse = DictReader(f)
    meteo = {int(code['Code temps']) : code['Description'] for code in reponse}

