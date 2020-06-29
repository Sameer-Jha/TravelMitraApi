#!/usr/bin/env python3 

import requests
import json
import csv
import os
import datetime
import creds
import busCityList

base_url='http://developer.goibibo.com/api/'

#City_code City_name dictionary
city_list_path = 'city_list.csv'
city_list_file = open(city_list_path,'r')
city_list = csv.reader(city_list_file,delimiter=',')
city_dictionary = {}
for i in city_list:
    city_dictionary[i[0].lower()] = i[1]

# date format for api (YYYYMMDD) => 20200705

def flight_search(src,dest,seating='E',adult=1,child=0,infant=0,date=''):
    if date=='' or date==None:
        x = datetime.datetime.now() + datetime.timedelta(days=1)
        date = x.strftime("%Y%m%d")
    request_url = f'{base_url}search/?app_id={creds.app_id}&app_key={creds.app_key}&format=json&source={src}&destination={dest}&dateofdeparture={date}&seatingclass={seating}&adults={adult}&children={child}&infants={infant}&counter=100'
    print(request_url)
    json_data = requests.get(request_url).content
    json_object = json.loads(json_data)
    json_format_data = json.dumps(json_object, indent=2)
    return(json_format_data) 

def bus_search(src,dest,date):
    src = busCityList.BusCity[src.upper()]
    dest = busCityList.BusCity[dest.upper()]
    request_url = f'{base_url}bus/search/?app_id={creds.app_id}&app_key={creds.app_key}&format=json&source={src}&destination={dest}&dateofdeparture={date}'
    print(request_url)
    json_data = requests.get(request_url).content
    json_object = json.loads(json_data)
    json_format_data = json.dumps(json_object, indent=2)
    return(json_format_data) 

def hotel_search(city):
    if city.lower() in city_dictionary.keys():
        city_id = city_dictionary[city.lower()]
        request_url = f'{base_url}voyager/get_hotels_by_cityid/?app_id={creds.app_id}&app_key={creds.app_key}&city_id={city_id}'
        print(request_url)
        json_data = requests.get(request_url).content
        json_object = json.loads(json_data)
        json_format_data = json.dumps(json_object, indent=2)
        return(json_format_data)
    else:
        return(f'https://www.google.com/travel/hotels/{city}') 

def main():
    pass
    # print(flight_search(src='IXR',dest='DEL'))
    # print(hotel_search('Prayagraj'))
    # print(bus_search('kanpur','lucknow',20200703))

if __name__ == "__main__":
    main()