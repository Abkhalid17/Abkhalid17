#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install requests')


# In[4]:


import datetime as dt
import requests

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'df2fc6ef79cdb2e6fcf2f459b2384970'

def get_weather_data(location):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    params = {'q': location, 'appid': API_KEY, 'units': 'metric'}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

def display_weather_info(weather_data):
    if not weather_data:
        return

    print(f"Weather in {weather_data['name']}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} km/h")

    
def main():
    location = input("Enter your city: ")
    weather_data = get_weather_data(location)

    if weather_data:
        display_weather_info(weather_data)

if __name__ == "__main__":
    main()


# In[ ]:




