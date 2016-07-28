from app import app, db
from .models import Player

from flask import render_template

@app.route('/')
@app.route('/home')
def home(): 
	return render_template('home.html', title = "Welcome to the gschouse!")

@app.route('/about')
def about():
	return render_template('about.html', title = "About the gschouse")

@app.route('/players')
def players():
	players = Player.query.all()
	return render_template('players.html', title = "Who we are", players = players)