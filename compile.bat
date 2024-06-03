@echo off
pyinstaller .\create_account.py
cls
echo "Finished compiling."
echo "Check the dist folder for the executable."
pause