from flask import *
import sqlite3


connection = sqlite3.connect('db.db', check_same_thread=False)
crsr = connection.cursor()

peers = []
messages=[]








peers.append("peer hna")
peers.append("peer akhor hna")
app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == "POST":

        text = request.form.get("text", False)
        password = request.form.get("password", False)
        print(password)
        print(text)
        text = request.form.get("text", False)
        public = request.form.get("join-public", False)
        if public != None:
            return redirect("/chat")



    return render_template("home.html")

@app.route("/submit_room", methods = ["POST", "GET"])
def submit_room():
    return '<input type="text" id="pwdtyper" class="typer" placeholder="Password" name="password">'






@app.route("/chat", methods = ["POST","GET"])
def chat():
    return render_template("chat.html", messages = messages, peers = peers)



@app.route("/submit_message", methods = ["POST", "GET"])
def submit_message():
    snd = ""

    message = request.data.decode('utf-8')
    messages.append(message)

    print(messages)

    return messages


@app.route('/update_section')
def update_section():

    html_content = ""
    for message in messages:
        html_content += f'<h1 class="messagee"> {message} </h1>'
    return html_content

if __name__ == "__main__":
    app.run(debug=True)

