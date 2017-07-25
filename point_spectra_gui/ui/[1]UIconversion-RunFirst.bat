md .\PythonUI
echo off && cls
for /r %%i in ("\UI Files\*.ui") do pyuic5 -x "%%i" > .\PythonUI\%%~ni.py