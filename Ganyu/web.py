from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/user')
def user():
    u = {
        'username': 'Ganyu',
        'uid': '100000'
    }
    return jsonify(u)

app.run("0.0.0.0",9090)