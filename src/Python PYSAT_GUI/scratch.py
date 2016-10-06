from pysat_function import pysat_func

# Initialize pysat for use


pysat = pysat_func()

#get all the files
[pysat.set_file_outpath(r'C:\Users\nfinch\Desktop\Output')
pysat.set_file_knowndatacsv(r'C:\Users\nfinch\Documents\GitHub\PySAT\src\Python PYSAT_GUI\full_db_mars_corrected_dopedTiO2_pandas_format.csv')
pysat.set_file_unknowndatacsv(r'C:\Users\nfinch\Documents\GitHub\PySAT\src\Python PYSAT_GUI\lab_data_averages_pandas_format.csv')
pysat.set_file_maskfile(r'C:\Users\nfinch\Documents\GitHub\PySAT\src\Python PYSAT_GUI\mask_minors_noise.csv')
pysat.get_spectra()
pysat.set_interp()
pysat.set_mask()
pysat.get_ranges([(0, 1000)])
pysat.set_element_name('SiO2')
pysat.set_nfolds(6)
pysat.set_testfold(4)
pysat.set_compranges([[-20, 50], [30, 70], [60, 100], [0, 120]])
pysat.set_stratified()
pysat.get_number_components([7, 7, 5, 9])
pysat.get_train_data()
pysat.get_test_data()
pysat.set_sm()
pysat.get_sm_fit()
pysat.get_plots()
]