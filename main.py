import tkinter as tk
from tkinter import ttk, messagebox
from contextlib import closing
from urllib.request import urlopen
import json
from lecture_csv import meteo

jeton = 'api_key'

with closing(urlopen(f'https://api.meteo-concept.com/api/location/city?token={jeton}&insee=14327')) as f:
    city = json.loads(f.read())['city']

with closing(urlopen(f'https://api.meteo-concept.com/api/forecast/daily/1?token={jeton}&insee=14327')) as f:
    decoded = json.loads(f.read())
    city, forecast = (decoded[k] for k in ('city', 'forecast'))

appli = tk.Tk()
appli.title('Météo du Jour')
appli.geometry('500x350')
appli.resizable(True, True)
appli.config(background='#2c2f33')

frame = tk.Frame(appli, bg='#2c2f33')
frame.pack(pady=20, padx=20, fill='both', expand=True)

# Titre principal
titre = tk.Label(frame, text=f"Météo à {city['name']}", font=("Helvetica", 18, 'bold'), fg='white', bg='#2c2f33', wraplength=450, justify='center')
titre.grid(row=0, column=0, pady=10)

# Date
date_label = tk.Label(frame, text=f"Date : {decoded['forecast']['datetime'][:10]}", font=("Helvetica", 12), fg='white', bg='#2c2f33')
date_label.grid(row=1, column=0, pady=5)

# Prévisions météo
meteo_label = tk.Label(frame, text=meteo[int(decoded['forecast']['weather'])], font=("Helvetica", 14), bg='#7289da', fg='white', height=3, width=40, relief='ridge')
meteo_label.grid(row=2, column=0, pady=15)

# Fonction pour afficher les dates futures
def afficher_dates_futures():
    with closing(urlopen(f'https://api.meteo-concept.com/api/forecast/daily?token={jeton}&insee=14327')) as f:
        future_data = json.loads(f.read())['forecast']
        dates = [item['datetime'][:10] for item in future_data]
        messagebox.showinfo("Dates futures", "\n".join(dates))

# Ajouter effet hover
def on_enter(e):
    e.widget.config(borderwidth=2, relief='solid')

def on_leave(e):
    e.widget.config(borderwidth=0, relief='flat')

# Bouton pour les dates futures
future_button = ttk.Button(frame, text="Voir les dates futures", command=afficher_dates_futures)
future_button.grid(row=4, column=0, pady=10)
future_button.bind("<Enter>", on_enter)
future_button.bind("<Leave>", on_leave)

# Bouton de sortie
quit_button = ttk.Button(frame, text="Quitter", command=appli.destroy)
quit_button.grid(row=5, column=0, pady=10)
quit_button.bind("<Enter>", on_enter)
quit_button.bind("<Leave>", on_leave)

# Lien API
api_label = tk.Label(appli, text='Source: meteo-concept.com', font=("Courier", 10), fg='#b9bbbe', bg='#2c2f33', cursor='hand2')
api_label.pack(side='bottom', pady=10)
api_label.bind("<Button-1>", lambda e: urlopen('https://api.meteo-concept.com/api/'))

appli.mainloop()
