from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def extract_usernames(raw_text):
    lines = raw_text.splitlines()
    usernames = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.lower() in ['remove', 'follow', 'following']:
            continue
        if line == line.lower() and re.match(r"^[a-z0-9._]{3,30}$", line):
            usernames.append(line)

    return usernames

@app.route('/')
def health_check():
    return jsonify({"status": "InstaCheck backend is running!"})

@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    followers_text = data.get("followers", "")
    following_text = data.get("following", "")

    followers = set(extract_usernames(followers_text))
    following = set(extract_usernames(following_text))

    not_following_back = list(following - followers)

    return jsonify({"not_following_back": not_following_back})

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
