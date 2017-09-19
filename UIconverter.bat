md .\ui
echo off && cls
for /r %%i in ("*.ui") do pyuic5 -x "%%i" > .\point_spectra_gui\ui\%%~ni.py