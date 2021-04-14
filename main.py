# Prints weather information for the next 5 days split in 3-hour segments
# For API information: https://openweathermap.org/forecast5
import requests
import json

if __name__ == '__main__':
    baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
    # In 'appid', insert your own key from OpenWeather
    parameters = {'q': 'Dublin,IE', 'appid': 'YOUR-KEY-HERE', 'units': 'metric'}
    response = requests.get(baseUrl, params=parameters)
    content = response.content
    # Parse json info
    info = json.loads(content)

    # To iterate through every timestamp
    list = info['list']
    for i in range(len(list)):
        listInfo = list[i]
        date = listInfo['dt_txt']
        mainData = listInfo['main']
        tempMax = mainData['temp_max']
        tempMin = mainData['temp_min']
        feelsLike = mainData['feels_like']
        weather = listInfo['weather']
        weatherDesc = weather[0]
        description = weatherDesc['description']

        print('Weather information for %s\nMax Temp: %sC, Min Temp: %sC, Feels like: %sC\nWeather description: %s\n' %
              (date, tempMax, tempMin, feelsLike, description))

    # print(listInfo)
