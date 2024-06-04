@echo off
pyinstaller .\create_account.py -y
cls
echo "Finished compiling."
echo "Check the dist folder for the executable."
pause