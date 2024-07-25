from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox

# Extract key from the configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# Function to get weather details
def getweather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin, temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")

# Function to search city
def search():
    city = city_text.get()
    weather = getweather(city)
    print(weather)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1]['country'])
        temperature_label['text'] = "Temperature: {:.2f} \u00B0C".format(weather[3])
        weather_l['text'] = "Weather: " + weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))

# Create Tkinter window
app = Tk()
app.title("Weather App")
app.geometry("500x350")
app.configure(bg='#f0f0f0')

# Styling options
label_font = ("Arial", 14)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Add widgets
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text, font=entry_font, bd=5, relief=GROOVE)
city_entry.pack(pady=10)

Search_btn = Button(app, text="Search Weather", width=15, command=search, font=button_font, bg='#4CAF50', fg='white', bd=0, relief=RIDGE)
Search_btn.pack(pady=10)

location_lbl = Label(app, text="Location", font=("Arial", 18, "bold"), bg='#f0f0f0', fg='#333')
location_lbl.pack(pady=10)

temperature_label = Label(app, text="", font=label_font, bg='#f0f0f0', fg='#333')
temperature_label.pack(pady=5)

weather_l = Label(app, text="", font=label_font, bg='#f0f0f0', fg='#333')
weather_l.pack(pady=5)

# Run the app
app.mainloop()
