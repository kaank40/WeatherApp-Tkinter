import requests
from tkinter import Tk, Entry, Button, Canvas
from PIL import Image, ImageTk  # Voor afbeeldingen

# API-sleutel en functie om weergegevens op te halen
api_key = '30d4741c779ba94c470ca1f63045390a'

def get_weather():
    city = city_entry.get()
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
    
    if weather_data.json()['cod'] == '404':
        canvas.itemconfig(result_text, text="Geen stad gevonden. Probeer opnieuw.")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        canvas.itemconfig(
            result_text, 
            text=f"Het weer in {city} is: {weather}\nTemperatuur: {temp}°C"
        )

# GUI-setup
root = Tk()
root.title("Weerapp")
root.geometry("400x600")

# Achtergrondafbeelding
background_image = Image.open(r"C:\Users\31639\Downloads\weather.gif")  # Correct pad
background_image = background_image.resize((400, 600), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(background_image)

canvas = Canvas(root, width=400, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Titeltekst op het canvas
canvas.create_text(200, 50, text="Weerapp", font=("Helvetica", 20, "bold"), fill="white")

# Invoerveld voor de stad
city_entry = Entry(root, font=("Helvetica", 14))
canvas.create_window(200, 100, window=city_entry)

# Knop om het weer op te halen
get_weather_button = Button(root, text="Haal weer op", command=get_weather, font=("Helvetica", 12))
canvas.create_window(200, 150, window=get_weather_button)

# Transparant ogende tekst voor resultaat
result_text = canvas.create_text(200, 200, text="", font=("Helvetica", 12), fill="white")

# Start de GUI
root.mainloop()