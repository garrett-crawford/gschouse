from app import app, db
from .models import Player
from .forms import PlayerForm

from flask import render_template, flash, redirect, url_for

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


@app.route('/add_player', methods = ['GET', 'POST'])
def addPlayer():
	form = PlayerForm()

	if form.validate_on_submit():
		player = Player(nickname = form.nickname.data, main = form.main.data, ranking = form.ranking.data, description = form.description.data)
		db.session.add(player)
		db.session.commit()

		flash("Added player to database")
		return redirect(url_for('players'))

	return render_template('addplayer.html', title = "Add Player", form = form)

@app.route('/rankings')
def rankings():
	players = Player.query.order_by(Player.ranking).all()

	return render_template('rankings.html', players = players)