from flask import Flask, render_template, request, redirect, url_for 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    text = db.Column(db.String(200)) 
    complete = db.Column(db.Boolean) 
  
# Route to index page with todo list.  
@app.route('/') 
def index(): 
    return render_template('index.html') 
  
# Route used to add items to todo list. 
@app.route('/add', methods =['POST']) 
def add(): 
    todo = Todo(text = request.form['todoitem'], complete = False) 
    db.session.add(todo) 
    db.session.commit() 
    
    return redirect(url_for('index')) # stay on the home page
  
if __name__ == '__main__': 
    app.run(debug = True) 
