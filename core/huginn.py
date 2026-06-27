#Imports
import threading
import time
from config import POLL_INTERVAL ,RECONNECT_DELAY


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
                #delay
                time.sleep(POLL_INTERVAL)
            except Exception as e:
                #error announced
                print(f"Huginn has lost sight: {e}")
                #retry after a delay
                time.sleep(RECONNECT_DELAY)
