import requests

# Enter the API key of Weatherstack here
api_key = "YOUR_WEATHERSTACK_API_KEY"

# Base URL for the Weatherstack API
root_url = "http://api.weatherstack.com/current?"

# Input the City name for which we need the weather data
city_name = input("Please Enter The City Name: ")
city_name.upper()

# Building the final URL for the API call
url = f"{root_url}access_key={api_key}&query={city_name}"

# Sending a get request to the URL
response = requests.get(url)

# Storing the returned JSON data into a variable
data = response.json()

# Checking if there is no error and the status code is 200
try:
    # Getting the temperature from the JSON data
    temp = data['current']['temperature']
    # Getting the pressure from the JSON data
    pressure = data['current']['pressure']
    # Getting the humidity from the JSON data
    humidity = data['current']['humidity']
    # Getting the weather description from the JSON data
    descr = data['current']['weather_descriptions'][0]
    # Getting the wind speed from the JSON data
    wind = data['current']['wind_speed']

    # Displaying all the data
    print(f"City Name: {city_name}")
    print(f"The Weather Condition is {descr}")
    print(f"The temperature is {temp} °C")
    print(f"The pressure is {pressure} hPa")
    print(f"The humidity is {humidity}%")
    print(f"The speed of the wind is {wind} m/s")

except KeyError as e:
    # If any error occurred or the key is not found in the JSON data, print this
    print("Something Went Wrong or City Not Found")
