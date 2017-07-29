@echo off
:top

@echo off
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)
git reset head~
git add -A
git commit -m "Update %mydate%_%mytime%"
git push -f
pause
goto :top
