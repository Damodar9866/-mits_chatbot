@echo off
title MITS Basic Chatbot Server
echo ===================================
echo   MITS Basic Chatbot Server Starting
echo ===================================
echo.
echo Installing/Updating dependencies...
pip install -r requirements.txt
echo.
echo Starting the basic chatbot server...
echo.
echo The chatbot will be available at:
echo   http://localhost:5000
echo   http://127.0.0.1:5000
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
