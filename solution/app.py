from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy  
  
app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
db = SQLAlchemy(app) 
  
class Todo(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    text = db.Column(db.String(200)) 
    complete = db.Column(db.Boolean) 
  
# Route to index page with todo list.  
@app.route('/') 
def index(): 
    incomplete = Todo.query.filter_by(complete = False).all() 
    complete = Todo.query.filter_by(complete = True).all() 
  
    return render_template('index.html',  
       incomplete = incomplete, complete = complete) 
  
# Route used to add items to todo list. 
@app.route('/add', methods =['POST']) 
def add(): 
    todo = Todo(text = request.form['todoitem'], complete = False) 
    db.session.add(todo) 
    db.session.commit() 
    
    return redirect(url_for('index')) # stay on the home page
  
# Route used to mark items as completed.
@app.route('/complete/<id>') 
def complete(id): 
    todo = Todo.query.filter_by(id = int(id)).first() 
    todo.complete = True
    db.session.commit() 

    return redirect(url_for('index')) # stay on the home page
  
if __name__ == '__main__': 
    app.run(debug = True) 
