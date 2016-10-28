UI Files holds many *.UI
	|_ process all these UI files with UIconversion.bat
		|_ UI conversion converts all the *.ui files to *.py and puts them into PythonUI
			|_ compare takes all the *.py files, and compares it against 10_mainwindow_empty_UI.py
				|_ take the differences and place them into FINISHED

All the files in FINISHED can then be copied and placed into their respective UI modules
