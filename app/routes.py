from flask import render_template, redirect, url_for, request, current_app as app
from app import get_db_connection

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/layout', methods=['GET', 'POST'])
def layout():
    return render_template('layout.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        number = request.form['number']
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (username, number) VALUES (%s, %s)", (username, number))
        connection.commit()
        cursor.close()
        connection.close()
        
        return redirect(url_for('welcome', username=username))
    
    return render_template('signup.html')

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)
