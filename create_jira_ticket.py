# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://[].atlassian.net/rest/api/3/issue"

apiToken=""

auth = HTTPBasicAuth("", apiToken)

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
              "text": "Kubernetes Kuadm Assignments",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
   
   
    "issuetype": {
      "id": "10005"
    },
  
    "project": {
      "key": "ST"
    },
    
    "summary": "First Jira Ticket", 
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

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))