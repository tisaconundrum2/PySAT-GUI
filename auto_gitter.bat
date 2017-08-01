@echo off
:top
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)
git add -A
git commit -m "Update %mydate%_%mytime%"
pause
goto :top
