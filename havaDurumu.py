from tkinter import *
from PIL import ImageTk, Image
import requests

api_key="14ed54e6cec0f6ee2c73701aa27d175a"
base_url= "http://api.openweathermap.org/data/2.5/weather?"
#q={city name}&appid={API key}

sehir_ismi=input("Şehir: ")
url=base_url+"appid="+api_key+"&q="+sehir_ismi

gelen_veri=requests.get(url)
json_veri=gelen_veri.json()

if json_veri["cod"] !="404":
    temp = json_veri["main"] ["temp"] #Kelvin'dan Çıkan Sonuç C°'ya Dönüştürme
    description=json_veri["weather"][0]["description"]
    pressure=json_veri["main"]["pressure"]
    country=json_veri["sys"]["country"]

    temp_in_celsius = float(temp) - 273.15
    
    print(f"temp: {temp_in_celsius:.2f}")
    print("description: "+str(description))
    print("pressure: "+str(pressure))
    print("country: "+str(country))
    

else :
    print("City not found")









"""
def get_weather():
    url = "https://api.openweathermap.org/data/3.0/onecall?lat=41.0082&lon=28.9784&exclude=minutely&appid=14ed54e6cec0f6ee2c73701aa27d175a&units=metric&lang=tr"
    url1=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    response = requests.get(url)
    weather_data = response.json()

    # Hava durumu verilerini işle
    current_weather = weather_data["current"]
    temp = current_weather["temp"]
    humidity = current_weather["humidity"]
    description = current_weather["weather"][0]["description"]

    # Pencereyi oluştur
    root = Tk()
    root.title("Hava Durumu")

    # Etiketleri ekle
    label_temp = Label(root, text=f"Sıcaklık: {temp}°C")
    label_temp.pack()

    label_humidity = Label(root, text=f"Nem: {humidity}%")
    label_humidity.pack()

    label_desc = Label(root, text=f"Açıklama: {description}")
    label_desc.pack()

    root.mainloop()

# Hava durumu verilerini almak için bir düğme oluştur
button = Button(text="Hava Durumu", command=get_weather)
button.pack()

mainloop()

"""