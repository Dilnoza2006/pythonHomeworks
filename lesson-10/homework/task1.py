import requests

API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = "Tashkent"
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    print("Failed to fetch weather data.")