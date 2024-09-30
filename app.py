from flask import Flask, json, jsonify
from flask_cors import CORS
import os


app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Define the path to dogs.json
DOGS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'dogs.json')

# Home route to load and send JSON data
@app.route('/')
def home():
    try:
        # Load the dogs.json file
        with open(DOGS_JSON_PATH, 'r') as file:
            dogs_data = json.load(file)
        
        # Send the data as a JSON response
        return jsonify(dogs_data)
    except FileNotFoundError:
        return jsonify({"error": "dogs.json file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in dogs.json"}), 500

if __name__ == '__main__':
    app.run(debug=True)