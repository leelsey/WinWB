# WinWB

### Windows Write Blocker
 External Storage Write Blocker for Windows OS

## 1. Tested environments
1) OS: Windows 7 and later
2) Python: 3.8.0 and later

## 2. Setup development environment
1) Setup python's virtual enviroment.
```powershell
python -m venv venv
```
2) Activate venv.
```powershell
.\venv\Scripts\Activate.ps1
```
If not did setup PowerSehll execution policy, try this berfore activate venv.
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
```
3) Install requirements.
```powershell
pip install -r requirements.txt
```

## 3. Interpreter run
### WinWB
1) Open Windows Terminal (PowerShell or CMD) with run as administrator.
2) Run script.
```bash
python .\winwb.py
```

## Build .exe file
### WinWB
1) Build through pyinstaller.
```powershell
pyinstaller --uac-admin --onefile --icon=.\images\logo.ico --name=WinWB winwb.py
```
2) It's created in the dist directory.
### WinWB-GUI
1) Build through pyinstaller.
```powershell
pyinstaller --uac-admin --onefile --windowed --icon=.\images\logo.ico --add-data="images;images" --name=WinWB-GUI winwb-gui.py
```
2) It's created in the dist directory.