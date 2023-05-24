# ElevenLabs-as-Microphone
Allows you to use an Elevenlabs voice as a microphone


# Installation Process
1) Download `FullInstaller.bat`, `Installscript.bat`, `SimpleElevenLabs.py` and `Start TTS.bat`
2) Run `FullInstaller.bat` AS ADMINISTRATOR. (This is because both Python and VB Audi Cable need to be installed as Administrator and saves the hiccups with that.)
3) When the Python installation starts, select `Add Python.exe to PATH`. Once the Installer is finished, Select `Change Path Limit`.

You are almost done. Rightclick the `SimpleElevenLabs.py` file and select `Open With`. Then select notepad.
You should see a line called 
`set_api_key("Enter Key Here")`
Replace the `Enter Key Here` with your Elevenlabs API key
(The Elevenlabs API requires a 5$ subscription monthly to be accessible.) <https://docs.elevenlabs.io/api-reference/quick-start/authentication>

You are now done. Simply run `Start TTS.bat` and it should work.
You can now select `CABLE Output` in any software that supports a microphone and start to talk through voicechat with your favorite voice!
