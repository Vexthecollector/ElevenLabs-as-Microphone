curl.exe -o VBCable.zip https://download.vb-audio.com/Download_CABLE/VBCABLE_Driver_Pack43.zip
mkdir VBCable
tar -zxvf VBCable.zip -C "%cd%\VBCable"

curl.exe -o PythonInstaller.exe https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe

"%cd%\VBCable\VBCable_Setup_x64.exe"
"%cd%\PythonInstaller.exe"