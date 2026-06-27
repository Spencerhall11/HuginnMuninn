#imports
import os
from dotenv import load_dotenv

#call the end load
load_dotenv()

#variables
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
TENANT_ID = os.getenv("AZURE_TENANT_ID")

#email filters
WHITELIST_SENDERS =[]
PRIORITY_KEYWORDS =["urgent","exam","application","applying","resume","important","critical"]
APPROVED_DOMAINS =["odu.edu","linkedin.com"]

#audio settings
TTS_VOLUME = 0.5

#connection settings
POLL_INTERVAL = 1800
RECONNECT_DELAY = 300