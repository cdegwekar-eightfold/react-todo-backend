from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy  
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)

#set database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#creating db instance
db = SQLAlchemy(app)


class ToDoTable(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.Text , nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'description'  : self.description
       }
    def __repr__(self):
        return f"Item('{self.id}','{self.description}')"

@app.route("/")
@cross_origin()
def home():
    task_list = ToDoTable.query.all() #filter
    # print( task_list)
    # return render_template('home.html', task_list = task_list)
    serialized_list = [t.serialize for t in task_list]
    # return {
    #   'resultStatus': 'SUCCESS',
    #   'message': "Hello Api Handler"
    #   }
    # return jsonify(task_list)
    return {'todo_list':serialized_list}


    # return render_template('./frontend/src/App.js')

@app.route('/add', methods=['POST'])
@cross_origin()
def add():
    post_data = request.json
    new_item = ToDoTable(description=post_data['description'])
    db.session.add(new_item)
    db.session.commit()
    # return redirect(url_for('home'))
    return 'success'

@app.route('/delete/<id>', methods=['POST']) #DELETE as per convention
def delete(id):
    print(id)
    delete_item = ToDoTable.query.get(id)
    db.session.delete(delete_item)
    db.session.commit()
    # return redirect(url_for('home'))
    return 'success'

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