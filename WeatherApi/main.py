import requests
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Hava Durumu")
root.minsize(400, 400)
root.resizable(False, False)

# Definasyonlar -------------------------------------------
def get_ip_location(ip_address=None):
    url = f"https://ipinfo.io/{ip_address}/json" if ip_address else "https://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()
    return data

def fetch_weather(city):
    api_key = "c928dd7d71d193046015397772c79ff2"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            raise Exception(data.get("message", "Unknown error"))
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]
        return temperature, weather_description, wind
    except Exception as e:
        messagebox.showerror("Error", f"Please enter a place in the world: {e}")
        return None, None, None

def startup_fetch_weather():
    location_data = get_ip_location()
    location = location_data.get('city', 'Unknown')
    return location

def update_weather_display():
    city = city_entry.get() if city_entry.get() else startup_fetch_weather()
    temperature, weather_description, wind = fetch_weather(city)
    if temperature is not None:
        weather_label.config(text=f"City: {city}\n"
                                  f"Temperature: {temperature}°C\n"
                                  f"Weather: {weather_description}\n"
                                  f"Wind: {wind} m/s")

# GUI -------------------------------------------
FONT = ('Arial', 16, 'bold')

city_label = tk.Label(
    root,
    text=f"City:{get_ip_location()['city']}",
    padx=20,
    pady=5,
    font=FONT
)
city_label.pack()

search_city = tk.Label(
    root,
    text="Search City: ",
    padx=20,
    pady=5,
    font=FONT
)
search_city.pack()

city_entry = tk.Entry(
    root,
    font=FONT
)
city_entry.pack(
    padx=20,
    pady=10
)

fetch_button = tk.Button(
    root,
    text="Fetch Weather",
    padx=20,
    pady=10,
    font=FONT,
    bg='gray',
    command=update_weather_display
)
fetch_button.pack()

weather_label = tk.Label(
    root,
    text="Weather...",
    padx=20,
    pady=10,
    font=FONT
)
weather_label.pack()

# Başlangıçta hava durumu verilerini güncelle
update_weather_display()

root.mainloop()
