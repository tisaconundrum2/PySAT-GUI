@echo off
:top

@echo off
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)
FOR /f "delims=" %%I in ('dir %USERPROFILE% /b/o/w/s ^| find /i "cmd\git.exe"') do (
%%I config remote.origin.url git@github.com:tisaconundrum2/PySAT_Point_Spectra_GUI.git
%%I  pull origin master
%%I  add -A
%%I  commit -m "Update %mydate%_%mytime%"
timeout /t 60
)
goto :top
