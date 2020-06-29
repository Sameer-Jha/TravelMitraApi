#!/usr/bin/env python3

from flask import Flask, request
import master

app = Flask(__name__)

@app.route('/')
def welcome():
    return('<h2>You are at the root of all cause 🙋</h2>')

@app.route('/hotel')
def hotel_booking():
    city=request.args.get('city')
    return(master.hotel_search(city))

@app.route('/flight')
def flight_booking():
    src=request.args.get('src')
    dest=request.args.get('dest')
    seating=request.args.get('class')
    date=request.args.get('date')
    return(master.flight_search(src,dest,seating,1,0,0,date))

@app.route('/bus')
def bus_booking():
    src=request.args.get('src')
    dest=request.args.get('dest')
    date=request.args.get('date')
    return(master.bus_search(src,dest,date))