::made by midnight
 
@echo off
setlocal enableextensions enabledelayedexpansion
del %temp%\tokenchecker.json /q /f
title Discord Token Checker
mode 102,22
chcp 65001>nul
color 0f
cls
echo.
echo.
echo             [40;35m█▀▄ █ █▀ █▀▀ █▀█ █▀█ █▀▄   ▀█▀ █▀█ █▄▀ █▀▀ █▄ █   █▀▀ █ █ █▀▀ █▀▀ █▄▀ █▀▀ █▀█
echo             [40;35m█▄▀ █ ▄█ █▄▄ █▄█ █▀▄ █▄▀    █  █▄█ █ █ ██▄ █ ▀█   █▄▄ █▀█ ██▄ █▄▄ █ █ ██▄ █▀▄
echo. 
echo                             [40;37mDrag the tokens file (.txt) to the console
echo.
echo.
set /p tpath="[40;30m.[40;37mPath: "
echo.
if not exist %tpath% echo  [40;31m[-] File not found &pause>nul & exit
for /F "usebackq tokens=*" %%T in ("%tpath%") do (
curl -s -H "Content-Type: application/json" -H "Authorization: %%T" https://discordapp.com/api/v8/users/@me > %temp%\tokenchecker.json
find /i "401: Unauthorized" %temp%\tokenchecker.json >nul
if errorlevel 1 (
echo  [40;32m[+] %%T
echo %%T>>hits.txt
) else (
echo  [40;31m[-] %%T
del %temp%\tokenchecker.json /q /f )
)
echo.
echo  [40;37mValid tokens have been saved in [40;32mhits.txt
pause>nul
exit