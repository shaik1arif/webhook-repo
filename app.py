from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import pytz
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Load MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
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

    print(f"\n🎯 Received GitHub Event: {event_type}")
    print(data)

    timestamp = datetime.now(pytz.UTC).strftime("%d %B %Y - %I:%M %p UTC")

    if event_type == "push":
        event_data = {
            "action": "push",
            "author": data["pusher"]["name"],
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": timestamp
        }
        collection.insert_one(event_data)
        print(f"✅ Push event stored: {event_data}")

    elif event_type == "pull_request":
        pr = data["pull_request"]
        action = data["action"]
        from_branch = pr["head"]["ref"]
        to_branch = pr["base"]["ref"]

        if action == "opened":
            event_data = {
                "action": "pull_request_opened",
                "author": pr["user"]["login"],
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
            collection.insert_one(event_data)
            print(f"✅ Pull request opened stored: {event_data}")

        elif action == "closed" and pr["merged"]:
            event_data = {
                "action": "merged",
                "author": pr["user"]["login"],
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
            collection.insert_one(event_data)
            print(f"✅ Merge event stored: {event_data}")

    return jsonify({"status": "success", "event": event_type}), 200

@app.route("/view")
def view():
    return render_template("index.html")

@app.route("/events")
def get_events():
    events = list(collection.find().sort("_id", -1))
    for event in events:
        event["_id"] = str(event["_id"])  # Convert ObjectId to string
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=True)
