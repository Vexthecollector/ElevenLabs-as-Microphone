# ElevenLabs-as-Microphone
Allows you to use an Elevenlabs voice as a microphone

# Requirements
1) An ElevenLabs subscription at the 5$ Tier or higher
2) Windows. I only got a windows PC to test these things on currently, so sadly it is only for windows. (The code is quite simple to adjust for linux though, as the only windows only requirement is VB Audio)

# Installation Process
1) Download `FullInstaller.bat`, `Installscript.bat`, `SimpleElevenLabs.py` and `Start TTS.bat` and `piano2.wav`
2) Run `FullInstaller.bat` AS ADMINISTRATOR. (This is because both Python and VB Audio Cable need to be installed as Administrator and saves the hiccups with that.)
3) When the Python installation starts, select `Add Python.exe to PATH`. Once the Installer is finished, Select `Change Path Limit`.

You are almost done. Rightclick the `SimpleElevenLabs.py` file and select `Open With`. Then select notepad.
You should see a line called 
`set_api_key("Enter Key Here")`
Replace the `Enter Key Here` with your Elevenlabs API key
(The Elevenlabs API requires a 5$ subscription monthly to be accessible.) <https://docs.elevenlabs.io/api-reference/quick-start/authentication>

You are now done. Simply run `Start TTS.bat` and it should work.
You can now select `CABLE Output` in any software that supports a microphone and start to talk through voicechat with your favorite voice!



If you like this, be sure to check out https://vb-audio.com/Cable/index.htm as it is one of the backbones for this project.
The software is donationware, so they rely on your donations to work.



# What does this truly do?
It will install Python and VB Audio Cable for you.
Then install via pip Elevenlabs, Sounddevice, Soundfile, and Numpy
The Start TTS.bat simply starts the python file I created.

The python file connects to the Elevenlabs API. It pulls all the voices you currently have and then allows you to choose.
Next it sets the Audio Device to be CABLE Input VB-Audio
And finally it just plays files through that Audio device for you to be able to put that out through any available place.
