from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Ensure the content type is correct (optional but good practice)
    if request.content_type != 'application/json':
        return jsonify({"error": "Invalid content type"}), 400

    # Parse request
    req = request.get_json(force=True)
    session_params = req.get("sessionInfo", {}).get("parameters", {})

    # Extract parameters
    category = session_params.get("category", "N/A")
    subcategory = session_params.get("subcategory_hw", "N/A")

    # Simulate ticket creation
    ticket_id = "SR-" + str(random.randint(1000, 9999))

    # Compose response
    fulfillment_text = f"""✅ Ticket Created!
🧾 Ticket ID: {ticket_id}
📁 Category: {category}
📂 Sub-category: {subcategory}
"""

    # Return fulfillment response in Dialogflow CX expected format
    return jsonify({
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [fulfillment_text]
                    }
                }
            ]
        }
    })

# Main entry point
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
