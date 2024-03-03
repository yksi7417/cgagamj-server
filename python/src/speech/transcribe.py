import os
import pyaudio
from vosk import Model, KaldiRecognizer

# Load the model
model = Model("model")

# Create a recognizer
rec = KaldiRecognizer(model, 16000)

# Define the audio format
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Process audio chunks in real-time
while True:
    data = stream.read(2000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())
