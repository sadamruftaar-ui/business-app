from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

leads_db = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/add-lead', methods=['POST'])
def add_lead():
    data = request.json
    lead_name = data.get('name')
    niche = data.get('niche')
    phone = data.get('phone')
    
    lead_info = {
        "name": lead_name,
        "niche": niche,
        "phone": phone,
        "status": "New",
        "follow_up": "Pending"
    }
    leads_db.append(lead_info)
    
    return jsonify({"success": True, "message": "Lead added successfully and AI will process WhatsApp message!"})

@app.route('/api/leads', methods=['GET'])
def get_leads():
    return jsonify(leads_db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
