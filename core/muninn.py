import threading
import queue
import pyttsx3
import speech_recognition as sr
from config import TTS_VOLUME



#main class for it
class Muninn(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        #keeps running
        self.running = True
        #queue
        self.alert_queue = queue.Queue()
        #initialize the TTS engine
        self.engine = pyttsx3.init()
        #set TTS Volume
        self.engine.setProperty("volume", TTS_VOLUME)



    def run(self):
        #while running
        while self.running:
            #check the queue
            try:
                alert = self.alert_queue.get(timeout=3)
                self.speak(alert)
            #if queue is empty pass
            except queue.Empty :
                pass

    #speech part 
    def speak(self,text):
        #Muninn speaks and its recorded in text
        print(f"Muninn speaks: {text}")
        #munin says it
        self.engine.say(text)
        #run and then wait
        self.engine.runAndWait()
        
        