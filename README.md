# GitHub Webhook Receiver – TechStaX Assessment

This Flask-based app receives GitHub webhook events (push, pull request, and merge) and stores them in MongoDB Atlas. A frontend UI displays recent events with automatic refresh.

## Live GitHub Trigger Repo
[`action-repo`](https://github.com/shaik1arif/action-repo) — used to trigger GitHub webhook events.

## Features
- Push event tracking
- Pull request event tracking
- Merge detection
- MongoDB Atlas integration
- Auto-refreshing UI (every 15 seconds)
- Flask backend with API support

## Tech Stack
- Python + Flask
- MongoDB Atlas
- GitHub Webhooks
- HTML, JavaScript

## How to Run Locally

1. Clone this repo  
   `git clone https://github.com/shaik1arif/webhook-repo`

2. Set up virtual environment  
   `python -m venv venv && venv\Scripts\activate`

3. Install dependencies  
   `pip install -r requirements.txt`

4. Run Flask app  
   `py app.py`

5. Open browser  
   [http://localhost:5000/view](http://localhost:5000/view)

Make sure MongoDB Atlas is properly connected in `app.py`, and the webhook is configured in your `action-repo` settings.

## To Test Webhook Events

Use the [`action-repo`](https://github.com/shaik1arif/action-repo) to:
- Push commits
- Open pull requests
- Merge PRs

Then check `/view` for live updates!
