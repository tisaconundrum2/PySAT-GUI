from pysat_function import pysat_func

# Initialize pysat for use


pysat = pysat_func()

# Build was successful

fun_list = []
arg_list = []
kw_list = []
# C:\Users\nfinch\Desktop\full_db_mars_corrected_dopedTiO2_pandas_format.csv
# C:\Users\nfinch\Desktop\lab_data_averages_pandas_format.csv
# C:\Users\nfinch\Desktop\mask_minors_noise.csv
arg_list.append([r"C:\Users\nfinch\Desktop\Output"])                                                                    # set_file_outpath
arg_list.append([r"C:\Users\nfinch\Desktop\full_db_mars_corrected_dopedTiO2_pandas_format.csv", "known data"])          # get_dat1a
arg_list.append(['known data', r"C:\Users\nfinch\Desktop\mask_minors_noise.csv"])                                       # do_mask
arg_list.append(['known data', [(0, 1000)]])                                                                            # do_norm
arg_list.append(['known data', 5, 2, ('meta', 'SiO2')])                                                                 # do_strat_folds1
arg_list.append(['known data', 'wvl', ('meta', 'SiO2'), 'PLS', {'n_components': 7, 'scale': False}, {}])                # do_regression_train
arg_list.append(['known data', 'PLS', 'wvl'])                                                                           # do_regression_predict
arg_list.append(['known data', ('meta', 'SiO2'), ('meta', 'PLS_prediction'), 'PLS_SiO2_nc7.png'])                       # do_scatterplot

kw_list.append({})                                                                                                      # set_file_outpath
kw_list.append({})                                                                                                      # get_dat1a
kw_list.append({})                                                                                                      # do_mask
kw_list.append({})                                                                                                      # do_norm
kw_list.append({})                                                                                                      # do_strat_folds
kw_list.append({})                                                                                                      # do_regression_train
kw_list.append({})                                                                                                      # do_regression_predict
kw_list.append({'one_to_one': True})                                                                                    # do_scatterplot

fun_list.append(pysat.set_file_outpath)
fun_list.append(pysat.get_data)
fun_list.append(pysat.do_mask)
fun_list.append(pysat.do_norm)
fun_list.append(pysat.do_strat_folds)
fun_list.append(pysat.do_regression_train)
fun_list.append(pysat.do_regression_predict)
fun_list.append(pysat.do_scatterplot)

for i in range(len(fun_list)):
    print(i)
    fun_list[i](*arg_list[i], **kw_list[i])
