from flask import Flask, render_template

app = Flask(__name__)

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
@app.route("/home")
def hello_world():
    return render_template('home.html', task_list = dummy_data)

@app.route("/about")
def about_page():
    return render_template('about.html',task_list = dummy_data)

if __name__ == '__main__':
    app.run(debug=True)