from flask import Blueprint, render_template, request, flash, redirect, url_for
import  requests
from app.db import db
from app.models.personaje import  Personaje
bp_personaje = Blueprint('bp_personaje', __name__)

@bp_personaje.route('/')
def index():
    personajes=db.personaje.find({})
    return render_template("listpersonales.html",personajes=personajes)

@bp_personaje.route("/insertdataapi",methods=['GET', 'POST'])
def insert_data_api():
    for  nupag in range(1,3):
        api_generacion = "https://rickandmortyapi.com/api/character/?page=" + str(nupag)
        response = requests.get(api_generacion)
        data = response.json()
        #print(data['results'])
        print(f"******")
        for personaje in data['results']:
            url_episodio=personaje['episode'][0]
            response_url = requests.get(url_episodio)
            data_episodio = response_url.json()
            personaje=Personaje(personaje['id'],personaje['name'],personaje['status'],
                                personaje['species'],personaje['location']['name'],personaje['image'],data_episodio['name'])
            db.personaje.insert_one(personaje.to_json())
    return "data_insertada"

@bp_personaje.route('/profile/<id>',methods=['GET'])
def profile(id):
    personaje = db.personaje.find_one({"id":int(id)})
    #listapersonaje=[]
    #for p in personaje:
    #    listapersonaje.append(p)
    return render_template("profile.html",personaje=personaje)






