md .\PythonUI
echo off && cls
for /r %%i in ("\UI Files\*.ui") do pyuic "%%i" > .\PythonUI\%%~ni.py

md .\Finished\
for /r %%i in (".\PythonUI\*.py") do findstr /v /g:".\PythonUI\10_mainwindow_empty_UI.py" "%%i" > ".\Finished\%%~ni.py"