# Webhook Receiver – TechStaX Developer Assessment

This project is a Flask-based GitHub webhook receiver that listens for **push**, **pull request**, and **merge** events and stores them in **MongoDB Atlas**. The stored events are displayed in a live-updating UI.

## Repositories

- Trigger repo: [action-repo](https://github.com/shaik1arif/action-repo)
- Webhook repo: This repository (`webhook-repo`)

## Features

- Receive and store GitHub webhook events
- Supports:
  - Push events
  - Pull request opened/closed
  - Merged pull requests (bonus)
- Stores data in MongoDB Atlas
- Auto-refreshing UI (every 15 seconds) using HTML + JavaScript
- Flask backend with two endpoints:
  - `/webhook` (for GitHub POSTs)
  - `/view` (frontend UI)

## Tech Stack

- Python 3
- Flask
- MongoDB Atlas
- HTML, JavaScript
- GitHub Webhooks

## How to Run Locally

1. Clone this repository
git clone https://github.com/shaik1arif/webhook-repo
cd webhook-repo

2. Create virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the Flask server
py app.py

Now open http://127.0.0.1:5000/view to view events.

## How to Trigger Events

Use action-repo to:
-Push a commit to any branch
-Open a pull request
-Merge a pull request
Each of these will trigger a webhook → Flask receives it → stores in MongoDB → shows in UI.

## Example UI Output

shaik1arif push to main on 07 July 2025 - 11:05 AM UTC
shaik1arif pull_request_opened from feature to main on 07 July 2025 - 11:15 AM UTC
shaik1arif merged from feature to main on 07 July 2025 - 11:20 AM UTC
