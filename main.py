from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook is live! Use POST /webhook"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    tag = req.get('fulfillmentInfo', {}).get('tag', '')
    params = req.get('sessionInfo', {}).get('parameters', {})

    if tag == 'create_ticket':
        category = params.get("category", "Not provided")
        subcategory = params.get("subcategory_hw") or params.get("subcategory_sw") or "Not provided"
        justification = params.get("justification", "Not provided")
        ticket_id = "SR-" + str(7000 + int.from_bytes(os.urandom(2), "big") % 1000)  # random ticket ID

        response_text = (
            f"✅ Ticket Created!\n"
            f"🧾 Ticket ID: {ticket_id}\n"
            f"📁 Category: {category}\n"
            f"📂 Sub-category: {subcategory}\n"
            f"📝 Justification: {justification}"
        )
    else:
        response_text = "Sorry, I didn’t understand your request."

    return jsonify({
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [response_text]
                    }
                }
            ]
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
