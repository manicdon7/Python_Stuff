import requests

def get_weather(location):
    api_key = "b1a8c101f4143bcc1d1620ebe045ccce"  # Replace this with your actual OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "units": "metric",
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_forecast(location):
    api_key = "b1a8c101f4143bcc1d1620ebe045ccce"  # Replace this with your actual OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": location,
        "units": "metric",
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def display_weather(weather_data):
    main = weather_data["weather"][0]["main"]
    description = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    print("Current Weather:")
    print(f"Main: {main}")
    print(f"Description: {description}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s\n")

def display_forecast(forecast_data):
    print("5-Day Forecast:")
    for forecast in forecast_data["list"][:5]:
        date = forecast["dt_txt"]
        weather = forecast["weather"][0]["main"]
        temp = forecast["main"]["temp"]
        print(f"{date}: {weather}, {temp}°C")

def main():
    location = input("Enter the city name: ")
    try:
        weather_data = get_weather(location)
        display_weather(weather_data)
        forecast_data = get_forecast(location)
        display_forecast(forecast_data)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
