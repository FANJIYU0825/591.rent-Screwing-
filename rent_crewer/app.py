from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from rent_crewer.db1 import search_enumera_reuslt,search_enumera_region

app = Flask(__name__)
conn = MongoClient('localhost', 27017)
db = conn['rent_591']
collection = db.rent

@app.route("/",methods = ['GET','POST'])#main page
def index():
    return "<a> hello</a>"
@app.route("/result",methods = ['GET','POST'])#main page
def search():
    if request.method == 'POST':
        region = request.form['email'] 
        regis = search_enumera_region(region)
        for regi in regis:
            lin_k=search_enumera_reuslt(regi) 
            return render_template ('search_result.html' , lin_k = lin_k)
            
@app.route("/<region>",methods = ['GET','POST'])#main page
def search_reg(region):
        
        regis = search_enumera_region(region)
        for regi in regis:
            lin_k=search_enumera_reuslt(regi) 
            return render_template ('search_result.html' , lin_k = lin_k)
            


if __name__ == '__main__':
    app.run(debug = True)
