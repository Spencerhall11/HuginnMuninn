import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

#load the model
def load_whisper_model():

    return WhisperModel("base", device="cpu", compute_type="int8")


#pull the audio
def record_audio(duration=3):
    sample_rate = 16000
    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
        device=1
    )
    sd.wait()
    return audio.flatten()

#transcribe the audio
def transcribe_audio(model, audio):
    segments, _ = model.transcribe(audio, language="en", vad_filter=False)
    segments = list(segments)  # force evaluation

    result = " ".join(segment.text for segment in segments).strip().lower()
    
    return result