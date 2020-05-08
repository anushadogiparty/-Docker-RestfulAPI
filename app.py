from flask import Flask, jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./cars.json').read())
data=jData["cars"]

# Intial request Ex: localhost:5000
@app.route('/')
def route_main():
    return "RESTful Webservice Started. Request data with proper URL"

# Returns JSON which containes car details
@app.route('/getcars/')
def cars_all():
    return render_template("index.html",items=data)

# Returns cars JSON which matches the id
@app.route('/getcars/<string:id>/')
def cars_by_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the cars JSON with particualr car Type
@app.route('/getcars/Car_Name/<string:Car_Name>/')
def cars_by_type(Car_Name=''):
    myList=[]
    for element in data:
        if element["Car_Name"].lower() == Car_Name.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the cars JSON with particualr Year
@app.route('/getcars/Year/<string:Year>/')
def cars_by_year(Year=''):
    myList=[]
    for element in data:
        if element["Year"].lower() == Year.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the cars JSON with particular car type and particular year 
@app.route('/getcars/Car_Name/<string:Car_Name>/Year/<string:Year>/')
def cars_by_car_type_and_year(Car_Name='', Year=''):
    myList=[]
    for element in data:
        if element["Car_Name"].lower() == Car_Name.lower():
             if element["Year"].lower() == Year.lower():
                myList.append(element)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
