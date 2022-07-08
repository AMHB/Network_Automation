import requests

apikey = 'd9018602f134baf49774b75cc467706e'
url = 'http://api.openweathermap.org/data/2.5/weather'

cities = ['Istanbul', 'Ankara', 'Antaliya', 'Paris', 'London',
          'Madrid', 'Berlin', 'Erzurum', 'Toronto', 'Helsinki']

for city in cities:
    response = requests.get(url,
                            params={'appid': apikey,
                                    'q': city,
                                    'units': 'metric'})

    if response.status_code == 200:
        weather = response.json()
        print(city,
              str(weather['main']['temp']) + '\u2103',
              ','.join([x['main'] for x in weather['weather']]))
    else:
        print(response.status_code)
