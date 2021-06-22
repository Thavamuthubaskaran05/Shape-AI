import requests

from datetime import datetime

api_key = '3c0cda3b2326161fafdda1d45186f367'
location = input("Enter the city name: ").lower()

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

l=[]
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

l.append("-------------------------------------------------------------")
l.append("Weather Report for - {}  || {}".format(location.upper(), date_time))

l.append("Current temperature is: {:.2f} deg C".format(temp_city))
l.append("Current weather desc  : {}".format(weather_desc))
l.append("Current Humidity      : {} %".format(hmdt))
l.append("Current wind speed    : {} coikmph".format(wind_spd))
print(l[0], "\n", l[1], "\n",l[0], "\n", l[2], "\n", l[3], "\n", l[4], "\n", l[5], "\n")
with open ("Weatherfinder.txt","a+") as weather:
    weather.writelines(l[0]+"\n")
    weather.writelines(l[1]+"\n")
    weather.writelines(l[0]+"\n")
    weather.writelines(l[2]+"\n")
    weather.writelines(l[3]+"\n")
    weather.writelines(l[4]+"\n")
    weather.writelines(l[5]+"\n\n")
