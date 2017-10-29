from flask import Flask, render_template
import random, socket

app = Flask(__name__)
ip = socket.gethostbyname(socket.gethostname())
word_count = 0;
used = []

with open("wordlist.txt","r") as f:
    for x in f:
        word_count += 1

@app.route("/")
def index():
    return render_template("./index.html",ip_addr=ip)

@app.route("/get_new_word")
def get_new_word():
    with open("wordlist.txt", "r") as words:
        num = random.randint(0, word_count)
        for i, line in enumerate(words):
            if line in used:
                num += 1;
            if i == num:
                used.append(i)
                return str(line).rstrip();

@app.route("/clearlist")
def clearlist():
    used = []
