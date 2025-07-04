from flask import Flask, render_template, request, redirect
import nltk  
from nltk.chat util
import Chat, reflections


################-------------------CHat Bot--------------############
rules = [
    (r"hello",["hi", "hello" ]),
    (r"ac is not working", ["pankha chalao","hmare yaha ais a hota h"])
]

my_chat_bot = Chat(rules)


################------------------------FLASK code------------------################
app = Flask(__name__)

@app.route('/')
def home():
    return "Home page"

@app.route('/chat', methods =['POST', 'GET'])
def chatbot():
    if request.method == "POST":
       ques = request.form['ask_me']
       print(ques)
       res = my_chat_bot.respond(ques)  
       print(res)
       return render_template("home.html",response_from_flask = res)
    else:
        return_render_template("home.html")

 app.run(debug=True)   