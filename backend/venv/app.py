from flask import Flask, request, jsonify
from pymongo import MongoClient
import psycopg2
import requests

app = Flask(__name__)

# MongoDB setup
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['flight_status']

@app.route('/api/flight-status', methods=['GET'])
def get_flight_status():
    flight_status = list(mongo_db.flight_status.find({}))
    return jsonify(flight_status)

@app.route('/api/send-notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    message = data['message']
    return jsonify({"status": "Notification sent", "message": message})


@app.route('/api/send-notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    message = data['message']
    fcm_url = 'https://fcm.googleapis.com/fcm/send'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=YOUR_SERVER_KEY',
    }
    payload = {
        'notification': {
            'title': 'Flight Status Update',
            'body': message,
        },
        'to': '/topics/all',
    }
    response = requests.post(fcm_url, json=payload, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
