from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import pytz

app = Flask(__name__)

# ✅ MongoDB connection string
MONGO_URI = "mongodb+srv://arif:arif123@cluster0.5v0yjx7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["webhookDB"]
collection = db["events"]

@app.route("/")
def home():
    return "Webhook receiver is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")
    timestamp = datetime.now(pytz.UTC).strftime("%d %B %Y - %I:%M %p UTC")

    if event_type == "push":
        author = data['pusher']['name']
        to_branch = data['ref'].split('/')[-1]

        event_data = {
            "action": "push",
            "author": author,
            "to_branch": to_branch,
            "timestamp": timestamp
        }
        collection.insert_one(event_data)
        print("✅ Push event stored:", event_data)

    elif event_type == "pull_request":
        action = data['action']
        pr = data['pull_request']
        author = pr['user']['login']
        from_branch = pr['head']['ref']
        to_branch = pr['base']['ref']

        if action == "closed" and pr.get("merged"):
            event_data = {
                "action": "merged",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
            print("✅ Merge event stored:", event_data)
        else:
            event_data = {
                "action": f"pull_request_{action}",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
            print("✅ Pull Request event stored:", event_data)

        collection.insert_one(event_data)

    return jsonify({"status": "stored", "event": event_type}), 200

@app.route("/events")
def get_events():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

@app.route("/view")
def view():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
