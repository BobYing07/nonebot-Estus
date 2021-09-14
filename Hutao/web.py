from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/user')
def user():
    u = {
        'username': 'Ganyu',
        'uid': '100000',
    }
    u2 = {
        'username': 'Beimo',
        'uid': '100001',
    }
    return jsonify(u,u2)

@app.route('/Ganyu')
def Ganyu():
    s1 = {
        's': '愿帝君保佑你'
    }

    s2 = {
        's': '名字是，王小美。甘雨？那是谁啊'
    }

    s3 = {
        's': '甘雨和王小美，根本一个字都没记对吧'
    }
    return jsonify(s1,s2,s3)





app.run("127.0.0.1",9090)