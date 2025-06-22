from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook is live! Use POST /webhook"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    tag = req.get('fulfillmentInfo', {}).get('tag', '')

    # Only handle the 'create_ticket' tag
    if tag == 'create_ticket':
        params = req.get('sessionInfo', {}).get('parameters', {})

        category = params.get('category', 'N/A')
        subcategory = params.get('subcategory', 'N/A')
        justification = params.get('justification', 'N/A')

        # Simulate ticket ID
        ticket_id = f"SR-{random.randint(1000, 9999)}"

        response_text = (
            f"✅ Ticket Created!\n"
            f"🧾 Ticket ID: {ticket_id}\n"
            f"📁 Category: {category}\n"
            f"📂 Sub-category: {subcategory}\n"
            f"📝 Justification: {justification}"
        )
    else:
        response_text = "Sorry, I didn’t recognize the request."

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
