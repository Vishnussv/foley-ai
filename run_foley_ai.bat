@echo off
TITLE Foley AI
echo Initializing Foley AI System...
echo.

:: Check if venv exists
if not exist "venv" (
    echo Virtual Environment not found! Please run installation steps first.
    pause
    exit
)

:: Activate venv and run app
call venv\Scripts\activate
cd backend

echo Killing old Foley processes...
taskkill /F /IM python.exe >nul 2>&1

echo Starting Server...
echo Access the Hologram Interface at: http://localhost:5000
echo.
python app.py

pause
