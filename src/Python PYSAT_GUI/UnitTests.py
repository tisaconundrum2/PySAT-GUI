from pysat_func import pysat_func

# Initialize pysat for use


pysat = pysat_func()

# Build was successful

fun_list = []
arg_list = []
kw_list = []

# 0
fun_list.append(pysat.set_file_outpath)
arg_list.append([r"C:\Users\nfinch\Desktop\Output"])
kw_list.append({})

# 1
fun_list.append(pysat.get_data)
arg_list.append([r"C:\Users\nfinch\Desktop\full_db_mars_corrected_dopedTiO2_pandas_format.csv", "known data"])
kw_list.append({})

# 2
fun_list.append(pysat.do_mask)
arg_list.append(['known data', r"C:\Users\nfinch\Desktop\mask_minors_noise.csv"])
kw_list.append({})

# 3
fun_list.append(pysat.submodel_ranges)
arg_list.append(['known data', [(0, 1000)]])
kw_list.append({})

# 4
fun_list.append(pysat.do_strat_folds)
arg_list.append(['known data', 5, 2, ('meta', 'SiO2')])
kw_list.append({})

# 5
fun_list.append(pysat.do_regression_train)
arg_list.append(['known data', 'wvl', ('meta', 'SiO2'), 'PLS', {'n_components': 7, 'scale': False}, {}])
kw_list.append({})

# 6
fun_list.append(pysat.do_regression_predict)
arg_list.append(['known data', 'PLS', 'wvl'])
kw_list.append({})

# 7
fun_list.append(pysat.do_scatterplot)
arg_list.append(['known data', ('meta', 'SiO2'), ('meta', 'PLS_prediction'), 'PLS_SiO2_nc7.png'])
kw_list.append({'one_to_one': True})


for i in range(len(fun_list)):
    print(i)
    fun_list[i](*arg_list[i], **kw_list[i])
