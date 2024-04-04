from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])
def createJIRA():

    url = "https://www.preethi-devops.com/syllabus/rest/api/3/issue"
    API_TOKEN=""
    auth = HTTPBasicAuth("", API_TOKEN)
    
    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }
    
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
                  "text": "My first jira ticket.",
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
          "key": "AAR"
        },
        "summary": "first jira ticket",
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

app.run('0.0.0.0', port=5000)