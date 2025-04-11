from flask import Flask, request
import json
import os
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()  # Get the incoming JSON data
    print(f"Received request body: {json.dumps(data)}")

    return "Processed request", 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))  # Default to port 8080 if not specified
    app.run(debug=False, host='0.0.0.0', port=port)
