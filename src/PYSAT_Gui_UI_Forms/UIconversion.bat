echo off && cls
:top
for /r %%i in ("\UI Files\*.ui") do pyuic "%%i" > .\PythonUI\%%~ni.py
timeout /t 3
goto :top