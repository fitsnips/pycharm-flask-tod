from flask import Flask, render_template, redirect, request

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flasktodos.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=False)
    is_completed = db.Column(db.Boolean)

    def __init__(self, title):
        self.title = title
        self.is_completed = 0


@app.route('/')
def hello_world():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    db.session.add(Todo(title=request.form['title']))
    db.session.commit()
    return redirect('/')

app.debug = True

if __name__ == '__main__':
    app.run()
