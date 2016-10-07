from pysat_function import pysat_func

# Initialize pysat for use


pysat = pysat_func()

# Build was successful

fun_list = []
fun_list.append(pysat.set_file_outpath(r'C:\Users\nfinch\Desktop\Output'))
fun_list.append(pysat.set_file_knowndatacsv(r'C:\Users\nfinch\Desktop\full_db_mars_corrected_dopedTiO2_pandas_format.csv'))
fun_list.append(pysat.set_file_unknowndatacsv(r'C:\Users\nfinch\Desktop\lab_data_averages_pandas_format.csv'))
fun_list.append(pysat.set_file_maskfile(r'C:\Users\nfinch\Desktop\mask_minors_noise.csv'))
fun_list.append(pysat.get_spectra())
fun_list.append(pysat.set_interp())
fun_list.append(pysat.set_mask())
fun_list.append(pysat.get_ranges([(0, 1000)]))
fun_list.append(pysat.set_element_name('SiO2'))
fun_list.append(pysat.set_nfolds(6))
fun_list.append(pysat.set_testfold(4))
fun_list.append(pysat.set_compranges([[-20, 50], [30, 70], [60, 100], [0, 120]]))
fun_list.append(pysat.set_stratified())
fun_list.append(pysat.get_number_components([7, 7, 5, 9]))
fun_list.append(pysat.get_train_data())
fun_list.append(pysat.get_test_data())
fun_list.append(pysat.set_sm())
fun_list.append(pysat.get_sm_fit())
fun_list.append(pysat.get_plots())

for f in fun_list:
    f
