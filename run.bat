@echo off
setlocal enabledelayedexpansion

REM Getting the location of the script
echo => Getting the location of the script
set "DIR=%~dp0"

REM Navigate to the bot's directory
echo => Navigating to the bot's directory
cd /d "%DIR%"

REM Run the Node.js application
echo => Checking the dependencies and installing
pip install -r requirements.txt

REM Running the bot.
echo => Starting the bot...
python src/app.py
