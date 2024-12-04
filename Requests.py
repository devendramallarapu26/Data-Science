import requests

# Your OpenWeatherMap API key (replace with your own)
api_key= '3f8c59f5544510156097fb3b5fe5de2e'

# Base URL for the OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Function to fetch weather data for a city
def get_weather(city_name):
    # Construct the final API URL
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"  # 'units=metric' for Celsius

    # Send a GET request to the OpenWeatherMap API
    response = requests.get(complete_url)

    # Convert the response to JSON format
    data = response.json()

    # Check if the response is successful
    if data["cod"] != "404":
        # Extract relevant weather information
        main_data = data["main"]
        weather_data = data["weather"][0]
        wind_data = data["wind"]

        # Get the temperature, pressure, humidity, description, and wind speed
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["description"]
        wind_speed = wind_data["speed"]

        # Print the weather data
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found!")

# Example usage
city_name = "HYDERABAD"  # Replace with any city of your choice
get_weather(city_name)
