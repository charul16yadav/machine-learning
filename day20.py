from flask import flask, render_template
app = Flask(__name__)

@app.route('/')
def some_function():
    return"Some message from flask"

@app.route('/home')
def some_function2(): 
    return render_template('home.html')  

app.run(debug=true)