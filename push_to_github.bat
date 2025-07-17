@echo off
echo MITS Chatbot - Push to GitHub
echo ================================
echo.
echo INSTRUCTIONS:
echo 1. First, create a new repository on GitHub.com
echo 2. Name it: mits-chatbot
echo 3. Do NOT initialize with README, .gitignore, or license
echo 4. Copy the repository URL from GitHub
echo.
set /p github_url="Enter your GitHub repository URL (e.g., https://github.com/username/mits-chatbot.git): "
echo.
echo Adding remote origin...
git remote add origin %github_url%
echo.
echo Pushing to GitHub...
git push -u origin main
echo.
echo Done! Your project is now on GitHub.
echo.
pause
