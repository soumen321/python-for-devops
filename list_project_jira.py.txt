# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

apiToken=""

url = "https://[].atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("", apiToken)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)

#name = output[0]["name"]
#print(name)

for name in range(len(output)):
  print(output[name]["name"])