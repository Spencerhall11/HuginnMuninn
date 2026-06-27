#Imports
import threading
import time
from config import POLL_INTERVAL, RECONNECT_DELAY, WHITELIST_SENDERS, PRIORITY_KEYWORDS, APPROVED_DOMAINS
from services.mail import fetch_emails


#main class for it
class Huginn(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        #keeps running
        self.running = True
        #track and prevent repeats for emails
        self.seen_ids = set()



    def run(self):
        while self.running:
            try:
                print("Huginn takes flight")

                #email parts
                emails = fetch_emails()
                for email in emails:
                    email_id=email.get("id")
                    if email_id in self.seen_ids:
                        continue
                    self.seen_ids.add(email_id)
                    sender = email.get("from", {}).get("emailAddress", {}).get("name", "Unknown")
                    subject = email.get("subject", "No Subject")
                    if self.should_alert(sender, subject):
                        print(f"Huginn returns: New message from {sender} — {subject}")

                #delay
                time.sleep(POLL_INTERVAL)
            except Exception as e:
                #error announced
                print(f"Huginn has lost sight: {e}")
                #retry after a delay
                time.sleep(RECONNECT_DELAY)

    def should_alert(self, sender, subject):
        # check 1: whitelist
        if sender in WHITELIST_SENDERS:
            return True
        # check 2: keywords
        if any(keyword.lower() in subject.lower() for keyword in PRIORITY_KEYWORDS):
            return True
        # check 3: domain
        if any(domain in sender for domain in APPROVED_DOMAINS):
            return True
        return False