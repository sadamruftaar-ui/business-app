
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/add-lead', methods=['POST'])
def add_lead():
    data = request.json
    name = data.get('name')
    niche = data.get('niche')
    phone = data.get('phone')
    
    response_message = f"Success! AI WhatsApp automation triggered for {name} ({niche})."
    
    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
