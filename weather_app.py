import requests

API_Key = "40b49da6c6834e36a6cfadb39fd815af"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Ask user for city
city = input("Enter city name: ")

# Build the query paramenters
params = {
    "q": city,
    "appid": API_Key,
    "units": "imperial"  # Use "imperial" for Fahrenheit
}

# Send the request
response = requests.get(BASE_URL, params=params)

# Handle response
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°F")
    print(f"Humidity: {humidity}%")
    print(f"Description: [description.capitalize()]")
else:
    print("\nCity not found or API error. Please check the city name or your API key.")
