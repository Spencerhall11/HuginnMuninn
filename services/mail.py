#imports
import msal 
import requests
from config import CLIENT_ID

#get token
def get_access_token():
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority="https://login.microsoftonline.com/consumers"
    )
    
    # Try to get token silently first
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(
            ["Mail.Read", "User.Read"],
            account=accounts[0]
        )
        if result:
            return result
    
    # Device code flow for first time auth
    flow = app.initiate_device_flow(scopes=["Mail.Read", "User.Read"])
    print(flow["message"])
    result = app.acquire_token_by_device_flow(flow)
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