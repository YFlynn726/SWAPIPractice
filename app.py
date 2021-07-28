from flask import Flask
from flask.templating import render_template
import requests
import json

app = Flask(__name__)

PLANET_URL = "https://swapi.dev/api/planets/"
FILM_URL = "https://swapi.dev/api/films/"
PEOPLE_URL = "https://swapi.dev/api/people/"

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/planets')
def get_planets():
    res = requests.get(PLANET_URL)

    if res.status_code == 200: 
        planet_json = res.json()
        return render_template('planets.html', planet_json=planet_json)
    else: 
        return "Sorry something went wrong."

@app.route('/people')
def get_people():
    res = requests.get(PEOPLE_URL)

    if res.status_code == 200:
        peoples = res.json()
        return render_template('people.html', peoples=peoples)
    else: 
        return "Sorry something went wrong."

@app.route('/films')
def get_films():
    res = requests.get(FILM_URL)

    if res.status_code == 200:
        films = res.json()
        return render_template('films.html', films=films)
    else: 
        return "Sorry something went wrong."