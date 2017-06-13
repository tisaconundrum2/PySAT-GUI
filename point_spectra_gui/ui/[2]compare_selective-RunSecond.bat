@echo off
md .\Finished\
set /p "or_file=Drag and drop original file here: "
for /r %%i in (".\PythonUI\*.py") do findstr /v /g:"%or_file%" "%%i" > ".\Finished\%%~ni.py"