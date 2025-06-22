from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    # Extract session parameters
    session_params = req.get("sessionInfo", {}).get("parameters", {})

    # Safely retrieve values
    category = session_params.get("category", "N/A")
    subcategory_hw = session_params.get("subcategory_hw")
    subcategory_sw = session_params.get("subcategory_sw")
    
    # Use subcategory based on category
    if category == "hardware":
        subcategory = subcategory_hw or "N/A"
    elif category == "software":
        subcategory = subcategory_sw or "N/A"
    else:
        subcategory = "N/A"

    # Generate ticket ID
    ticket_id = f"SR-{random.randint(1000, 9999)}"

    # Create response text
    response_text = (
        f"✅ Ticket Created!\n"
        f"🧾 Ticket ID: {ticket_id}\n"
        f"📁 Category: {category}\n"
        f"📂 Sub-category: {subcategory}"
    )

    # Return the response
    return jsonify({
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": ["Here are the details:"]
                    }
                },
                {
                    "text": {
                        "text": [response_text]
                    }
                }
            ]
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
