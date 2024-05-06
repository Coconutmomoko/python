# 1
import requests


def get_weather():
    api_key = '6aa80129441d87972179f4486eed5318'
    city = input("Enter the name of a municipality: ")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if 'weather' in data:
        weather_description = data['weather'][0]['description']
        temperature_celsius = data['main']['temp'] - 273.15
        print(f"Weather condition: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f} °C")
    else:
        print("Unable to fetch weather information for the specified location.")


get_weather()

# 2
from geopy.distance import geodesic
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='airport',
         user='dbuser',
         password='123456',
         autocommit=True
         )


def coordinates(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def distance(icao1,icao2):
    coordinates1 = coordinates(icao1)
    coordinates2 = coordinates(icao2)
    return geodesic(coordinates1,coordinates2).kilometers




icao1 = input("Please enter the ICAO for the first airport:")
icao2 = input("Please enter the ICAO for the second airport:")

distance_km = distance(icao1, icao2)

print("The distance between the two airports is:", distance_km, "kilometers")

# 3
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='airport',
    user='dbuser',
    password='123456',
    autocommit=True
)

@app.route('/')
def home():
    return jsonify({"message": "Please call the airport API"})

@app.route(rule='/airport/<icao>', methods=['GET'])
def get(icao):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM airport WHERE ident = "{icao}"')
    airport_info = cursor.fetchone()

    if airport_info:
        response = {
            "ICAO": airport_info['ident'],
            "Name": airport_info['name'],
            "Location": airport_info['municipality']
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)









