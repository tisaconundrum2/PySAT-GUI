md .\ui
echo off && cls
for /r %%i in ("*.ui") do pyuic5 -x "%%i" > .\ui\%%~ni.py