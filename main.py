from flask import Flask,jsonify
from flask import render_template
from flask import request
import json
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/getStudioIdAndCustomerId',methods = ['GET'])
def getStudioIdCustomerId():
   studioId = request.args.get("studioId")
   customerId = request.args.get("customerId")
   return jsonify({"Data" : {
       "studioId" : studioId,
       "customerId" : customerId
   }})

if __name__ == '__main__':
   app.run(debug=True)