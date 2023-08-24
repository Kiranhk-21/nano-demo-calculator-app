from flask import Flask,request, jsonify

app = Flask(__name__) 


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.json
    return {"result": data["first"]+data["second"]}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data=request.json
    return {"result": data["first"]+data["second"]}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
