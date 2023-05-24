from elevenlabs import voices, generate, save, set_api_key
from elevenlabs.api import History
import sounddevice as sd
import soundfile as sf
import os

sd.default.device ="CABLE Input (VB-Audio Virtual Cable), Windows Directsound"
set_api_key("Enter Key Here")
voices = voices()
number=0
for voice in voices:
    print("[",number,"]",voice.name)
    number=number+1
while True:
    try:   
        voicenumber=int(input('Select Voice Number:'))
        break
    except:
        print("Please Enter a number")
def play_Audio():
    audio = generate(text=newtext, voice=voices[voicenumber])
    if os.path.exists("currentfile.mp3"):
        os.remove("currentfile.mp3")
    save(audio,"currentfile.mp3")
    data, fs = sf.read("currentfile.mp3", dtype="float32")
    sd.play(data,fs)
    
while True:
    newtext=input('Write Text:')
    try:
        play_Audio()
    except KeyboardInterrupt:
        print("Audio Interrupted")
    
    

