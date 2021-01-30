from flask import Flask,jsonify
from flask import render_template
from flask import request
import json
import os
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/getStudioIdCustomerIdalbumId',methods = ['GET'])
def getStudioIdCustomerIdalbumId():
   studioId = request.args.get("studioId")
   customerId = request.args.get("customerId")
   albumId = request.args.get("albumId")
   return jsonify({"Data" : {
       "studioId" : studioId,
       "customerId" : customerId,
       "albumId" : albumId
   }})

port = int(os.environ.get('PORT', 8000))

if __name__ == '__main__':
   # app.run(host='0.0.0.0', port=port)
   app.run(debug=True)
