from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

with open('file.txt','r') as file:
    conversation = file.read()

bott = ChatBot("Healthcare Chatbot System")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(bott.get_response(userText))

@app.route("/")
def home(): 
	return render_template("home.html")



if __name__ == "__main__":
	app.run()