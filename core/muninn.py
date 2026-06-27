import threading
import queue
import pyttsx3
import speech_recognition as sr
from config import TTS_VOLUME
from services.voice import load_whisper_model, record_audio, transcribe_audio



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
        #intialize whisper
        self.whisper = load_whisper_model()



    def run(self):
        #listen thread
        listen_thread = threading.Thread(target=self.listen_loop, daemon=True)
        listen_thread.start()
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
        
    def listen_loop(self):
        while self.running:
            try:
                #record audio
                audio = record_audio(duration=3)
                #transcribe audio
                text = transcribe_audio(self.whisper, audio)
                #check for wake up word
                if "hey muninn" in text:
                #if woken, record command
                    self.speak("Muninn listens")
                    command_audio = record_audio(duration=4)
                    command = transcribe_audio(self.whisper, command_audio)
                    self.handle_command(command)
            except Exception  as e:
                print(f"Muninn listen error: {e}")
        
    def handle_command(self, command):
        #munnin recieves the command
        print(f"Muninn received command: {command}")
        #pre-listed commands
        if "pause" in command:
            self.speak("Pausing playback")
        elif "read" in command:
            self.speak("Reading email")
        elif "open" in command:
            self.speak("Opening email")
        else:
            self.speak("Muninn does not understand")    