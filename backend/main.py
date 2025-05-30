from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://instacheck.us", "https://www.instacheck.us"]}})

def extract_usernames(raw_text):
    lines = raw_text.splitlines()
    usernames = []

    for line in lines:
        line = line.strip()

        if re.match(r"^[a-zA-Z0-9._]{3,30}$", line):
            usernames.append(line)

    return usernames

@app.route('/')
def health_check():
    return jsonify({"status": "InstaCheck backend is running!"})

@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    print("Incoming Data:", data)
    followers_text = data.get("followers", "")
    following_text = data.get("following", "")

    followers = set(u.lower() for u in extract_usernames(followers_text))
    following = set(u.lower() for u in extract_usernames(following_text))

    not_following_back = list(following - followers)

    return jsonify({"not_following_back": not_following_back})

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
