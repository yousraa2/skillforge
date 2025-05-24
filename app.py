from flask import Flask, render_template, request, jsonify
from ai_utils import ask_ai

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["GET"])
def chat_page():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").strip()
    topic = data.get("topic", "")

    # Format only if not already formatted
    if topic == "quiz":
        prompt = f"Generate a 5-question multiple choice quiz on: {user_message}"
    elif topic == "lesson":
        prompt = f"Create a personalized lesson plan to learn: {user_message}"
    elif topic == "explain":
        prompt = f"Explain in simple terms: {user_message}"
    else:
        prompt = f"Answer clearly and briefly: {user_message}"

    response = ask_ai(prompt)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
