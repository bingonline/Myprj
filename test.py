from flask import Flask
from flask import render_template
from flask import json,jsonify
import MyJson

app=Flask(__name__)


@app.route('/')
def hello():
    return render_template('basic.html')

@app.route('/data',methods=['POST','GET'])
def GetData():
    a=[]
    data1 = {'user': 789, 'email': 456, 'date': 123}
    a.append(data1)
    a.append(data1)
    return jsonify(a)



if __name__=='__main__':
    app.run(debug=True)