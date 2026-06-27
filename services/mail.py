#imports
import msal 
import requests
from config import CLIENT_ID,CLIENT_SECRET,TENANT_ID

#get token
def get_access_token():
    app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=f"https://login.microsoftonline.com/{TENANT_ID}",
    client_credential=CLIENT_SECRET
    )
    
    #get token
    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    return result

def fetch_emails():

    #get token
    token = get_access_token()
    if "access_token" not in token:
        raise Exception("Authentication failed")

    #add headers
    headers = {"Authorization": f"Bearer {token['access_token']}"}

    #requests
    response = requests.get(
    "https://graph.microsoft.com/v1.0/me/messages",
    headers=headers,
    params={"$top": 10, "$orderby": "receivedDateTime desc"}
    )

    #data results
    data = response.json()
    return data.get("value",[] )