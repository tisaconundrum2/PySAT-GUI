from pysat_function import pysat_func

# Initialize pysat for use
pysat = pysat_func()

#get all the files
pysat.set_file_outpath(r'C:\Users\nfinch\Desktop\Output')
pysat.set_file_db(r'C:\Users\nfinch\Documents\GitHub\PySAT\src\Python PYSAT_GUI\full_db_mars_corrected_dopedTiO2_pandas_format.csv')
pysat.set_file_unknowndatacsv(r'C:\Users\nfinch\Documents\GitHub\PySAT\src\Python PYSAT_GUI\lab_data_averages_pandas_format.csv')
pysat.set_file_maskfile(r'C:\Users\nfinch\Documents\GitHub\PySAT\src\Python PYSAT_GUI\mask_minors_noise.csv')


pysat.get_spectra()
pysat.set_interp()
pysat.set_mask()
pysat.get_ranges()