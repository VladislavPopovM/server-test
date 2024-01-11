from flask import Flask, request
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)
load_dotenv()

def get_external_version():
    """Sends a GET request to an external service and returns the response."""
    external_url = os.getenv("EXTERNAL_SERVICE_URL")  # Get URL from environment variable
    if not external_url:
        return "External service URL not configured"

    try:
        response = requests.get(external_url)
        return response.json()
    except requests.RequestException as e:
        return f"Error making request to external service: {e}"

@app.route("/version", methods=["GET", "POST"])
def version():
    if request.method == "POST":
        # Processing incoming POST request
        data = request.json
        return "Data received: " + str(data)
    else:
        # Processing GET request - send a request to an external service
        external_version = get_external_version()
        return "Response from external service: " + external_version

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5010)
