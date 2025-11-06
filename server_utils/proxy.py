from flask import Flask, Response, jsonify
# import requests

app = Flask(__name__)

# TARGET = "https://URL"

@app.route("/commands")
def proxy_commands():
    # try:
    #     r = requests.get(TARGET, timeout=5)
    #     return Response(r.content, status=r.status_code, content_type=r.headers.get("Content-Type"))
    # except requests.RequestException as e:
    #     return Response(f"Error fetching target: {e}", status=500)

    data = [
        {"command": "heal", "effect": 1},
        {"command": "burn"},
        {"command": "heal", "effect": 1},
        {"command": "burn"}
    ]

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3087)
