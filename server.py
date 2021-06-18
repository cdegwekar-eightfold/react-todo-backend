from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)
#set database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'

#creating db instance
db = SQLAlchemy(app)


class ToDoTable(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.Text , nullable=False)

    def __repr__(self):
        return f"Item('{self.id}','{self.description}')"


dummy_data = [
    {
        'description':"Task 1",
        'completed':False
    },
    {
        'description':"Task 2",
        'completed':True
    },
    {
        'description':"Task 3",
        'completed':False
    },
    {
        'description':"Task 4",
        'completed':True
    },

]


@app.route("/")
def home():
    task_list = ToDoTable.query.all()
    print( task_list)
    return render_template('home.html', task_list = task_list)

@app.route('/add', methods=['POST'])
def add():
    new_item = ToDoTable(description=request.form['new_item'])
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)


'''
from server import db
db.create_all()
from server import ToDoTable
item1 = ToDoTable(description='Task 1')

item2 = ToDoTable(description='Task 2')
item3 = ToDoTable(description='Task 3')
item4 = ToDoTable(description='Task 4')
db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.add(item4)

db.session.commit()

ToDoTable.query.all() # returns list of entries

'''