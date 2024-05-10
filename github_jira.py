# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask
import json

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    url = "https://[].atlassian.net/rest/api/3/issue"

    API_TOKEN=""

    auth = HTTPBasicAuth("", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
    "description": {
        "content": [
            {
                "content": [
                    {
                        "text": "Order entry fails when selecting supplier.",
                        "type": "text"
                    }
                ],
                "type": "paragraph"
                }
            ],
        "type": "doc",
            "version": 1
    },
    "project": {
        "key": "ST"
    },
    "issuetype": {
        "id": "10005"
    },
    "summary": "Main order flow broken",
    },
    "update": {}
    } )


    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    
app.run(host='0.0.0.0',port=5000)