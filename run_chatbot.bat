@echo off
title MITS Chatbot Server
cd /d "C:\Users\damod\mits_chatbot"
echo ===================================
echo    MITS Chatbot Server Starting
echo ===================================
echo.
echo Current directory: %CD%
echo.
echo Installing/Updating dependencies...
pip install -r requirements.txt
echo.
echo Starting the chatbot server...
echo.
echo The chatbot will be available at:
echo   http://localhost:5000
echo   http://127.0.0.1:5000
echo.
echo Press Ctrl+C to stop the server
echo.
python enhanced_app.py
pause
