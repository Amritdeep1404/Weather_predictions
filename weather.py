import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, location):
        params = {
            'q': location,
            'appid': self.api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def display_weather(self, weather_data):
        if weather_data:
            city = weather_data['name']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("Could not retrieve weather data. Please check the location.")

def main():
    api_key = "317637f2f896c913edc5bbd2d68fd8ac"  # Replace with your OpenWeatherMap API key
    weather_app = WeatherApp(api_key)

    while True:
        location = input("Enter a city name or coordinates (lat,lon) or 'exit' to quit: ")
        if location.lower() == 'exit':
            break
        weather_data = weather_app.get_weather(location)
        weather_app.display_weather(weather_data)

if __name__ == "__main__":
    main()
