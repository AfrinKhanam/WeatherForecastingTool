import argparse
import pyowm 
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--CityName", help="Provide City Name", required=True)
    args = parser.parse_args()
    city_name = args.CityName
    # API_KEY = os.environ.get("OWM_API_KEY")
    API_KEY = "5adaceb79e5cb497b69d64fa00f45b01"

    owm = pyowm.OWM(API_KEY)
    weather_mgr = owm.weather_manager()
    observation = weather_mgr.weather_at_place(city_name)
    temperature = observation.weather.temperature("celsius")["temp"]
    humidity = observation.weather.humidity
    wind = observation.weather.wind()
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
    print(f'Wind Speed: {wind["speed"]} m/s')
   
