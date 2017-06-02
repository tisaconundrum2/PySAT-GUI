@echo off
:top
for /f "delims=" %%I in ('dir %USERPROFILE% /b/o/w/s ^| find /i "cmd\git.exe"') do (
	%%I config remote.origin.url git@github.com:tisaconundrum2/PySAT_Point_Spectra_GUI.git
	%%I push -u origin dev
	timeout /t 60
)
goto :top
