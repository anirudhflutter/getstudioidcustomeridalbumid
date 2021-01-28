from flask import Flask,jsonify
from flask import render_template
from flask import request
import json
import os
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

port = int(os.environ.get('PORT', 8000))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=port)