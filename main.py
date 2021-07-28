import requests

# url = "https://swapi.dev/api/"

# response = requests.get(url)
# res = response.json()['films']
# print(res)

# films = requests.get(res)

# if films.status_code == 200: 
#     film_json = films.json()

#     for film in film_json['results']:
#         print(film['title']) 

# url = "https://swapi.dev/api/planets"

# response = requests.get(url)

# if response.status_code == 200:
#     planet_json = response.json() 

#     for planet in planet_json['results']:
#         print(planet['name'])

req = requests.get("https://swapi.dev/api/people")
# res = req.json()['films']
# films = requests.get(res)
data = req.json()['results']
for film in data['films']:
    print(data['films'][0])
# print(data['films'])