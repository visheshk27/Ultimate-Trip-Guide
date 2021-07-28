import requests, json


def places():
  api_key = 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3'

  url = "https://search-maps.yandex.ru/v1/?"

  query = str(input('Search query: '))

  response = requests.get(url + 'text=' + query +	'&type=geo&lang=en_US&apikey=' + api_key)
  print(response)
  x = response.json()
  print(x)

  y = x['features']
  print(y)


  for i in range(len(y)):
	
	  print(y[i]['properties']['name'])
   