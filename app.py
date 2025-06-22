from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import chatbot_response

app = Flask(__name__)
CORS(app)  # Allow React frontend

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message")
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
