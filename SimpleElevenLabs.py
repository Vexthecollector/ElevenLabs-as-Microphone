from elevenlabs import voices, generate, save, set_api_key
from elevenlabs.api import History
import sounddevice as sd
import soundfile as sf
import os
import time

voicenumber=0

def Select_Audio_Output():
    while True:
        devices=sd.query_devices()
        number=0
        for device in devices:
            if device['max_output_channels'] > 0:
                print("[",number,"]",device['name'])
                number=number+1
        while True:
            try:   
                voicenumber=int(input('Select Output Number:'))
                break
            except:
                print("Please Enter a number")

        sd.default.device = voicenumber
        try:
            data, fs = sf.read("piano2.wav", dtype="float32")
            sd.play(data,fs)
            time.sleep(1)
            text= input("Could you hear that sound? Type Yes if you did: ") 
            if text=="Yes" or text=="yes" or text=="Y" or text=="y":
                break
        except sd.PortAudioError:
            print("Looks like that did not work, please select a different output device.")

set_api_key("Enter Key Here")
def Select_Voice():
    voicelist = voices()
    number=0
    for voice in voicelist:
        print("[",number,"]",voice.name)
        number=number+1
    while True:
        try:   
            voicenumber=int(input('Select Voice Number:'))
            return voicelist[voicenumber]
            break
        except:
            print("Please Enter a number")

Select_Audio_Output()
selected_Voice=Select_Voice()

def play_Audio():
    audio = generate(text=newtext, voice=selected_Voice)
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
    
    

