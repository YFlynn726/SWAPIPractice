from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

URL ="https://swapi.dev/api/planets"

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/planets', methods=["GET"])
def get_planets():
    req = requests.get(URL)
    if req.status_code == 200:
        planet_json = req.json() 
        return render_template('planets.html', planet_json=planet_json)
    else: 
        return "Sorry no data today!"

@app.route('/films', methods=["GET"])
def get_films():
    req = requests.get("https://swapi.dev/api/films")
    if req.status_code == 200:
        films = req.json()
        return render_template('films.html', films=films)
    else: 
        return "Sorry no data today!"
        
@app.route('/people')
def get_people():
    req = requests.get("https://swapi.dev/api/people")


    if req.status_code == 200: 
        peoples = req.json()
        return render_template('people.html', peoples=peoples)

# @app.route('/people/details')
# def get_people_details():
#     req = requests.get("https://swapi.dev/api/people")

#     if req.status_code == 200: 
#         peoples = req.json()
#         return render_template('people.html', peoples=peoples)


