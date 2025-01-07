import tkinter as tk
from contextlib import closing
from urllib.request import urlopen
import json
from lecture_csv import meteo

jeton = '47a8503ffd4fce6772e915c4823da9d20afa33f75701c75bbe4843bf1f25f2d5'

with closing(
        urlopen(f'https://api.meteo-concept.com/api/location/city?token={jeton}&insee=14327')) as f:
        city = json.loads(f.read())['city']


appli = tk.Tk()
appli.title('Météo')
appli.config(background='#36393f')

with closing(
     urlopen(f'https://api.meteo-concept.com/api/forecast/daily/1?token={jeton}&insee=14327')) as f:
    decoded = json.loads(f.read())
    (city, forecast) = (decoded[k] for k in ('city', 'forecast'))

temps_meteo = decoded['forecast']['weather']

tk.Button(appli, text="Quitter", command=appli.destroy).grid(column=0, row=10)
tk.Label(appli, text=city['name'], fg='red', bg='#36393f').grid(row=1, column=0)
tk.Label(appli, text=decoded['forecast']['datetime'][:10:]).grid(row=2, column=0)
tk.Label(appli, text=meteo[int(temps_meteo)],bg='#2d2f34',fg='white',height=3,width=50).grid(row=3, column=0)
tk.Label(appli,text='https://api.meteo-concept.com/api/',font=("Courier", 10), fg='white',bg='#36393f').grid(row=20, column=0)

appli.mainloop()