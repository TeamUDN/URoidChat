from flask import Flask, render_template, jsonify, request,session
import json
from chat import response
import os
import random, string
app = Flask(__name__)

app.secret_key = 'secret'
#app.permanent_session_lifetime = timedelta(minutes=5)
def randomname(n=5):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

@app.route('/')
def index():
    #return "Hello World"
    session['user_name'] = 'master'
    session['bot_name'] = 'bot'
    return render_template("chat.html")


@app.route('/rename', methods=['POST'])
def rename():
    session['user_name'] = request.form['user_name']
    session['bot_name'] = request.form['bot_name']

    print(session['user_name'])
    print(session['bot_name'])

    #return render_template("chat.html")
    return ""


# /showにPOSTリクエストが送られたら処理してJSONを返す
@app.route('/show', methods=['POST'])
def show():
    u_name=session['user_name']
    b_name=session['bot_name']
    res = response(request.form['chatMessage'],u_name,b_name)

    return_json = {
        "message": res
    }

    return jsonify(values=json.dumps(return_json))


@app.route('/upload', methods=['POST'])
def upload():
    the_file = request.files['the_file']


    random=randomname(n=5)
    path=f'./static/models/upload{random}.vrm'
    the_file.save(path)

    return_json = {
        "path": path
    }
    
    return jsonify(values=json.dumps(return_json))


if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host="0.0.0.0", port=port)
    app.run()
