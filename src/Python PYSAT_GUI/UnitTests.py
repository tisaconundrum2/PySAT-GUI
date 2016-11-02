from pysat_func import pysat_func

# Initialize pysat for use


pysat = pysat_func()

# Build was successful

fun_list = []
arg_list = []
kw_list = []
# C:\Users\nfinch\Desktop\full_db_mars_corrected_dopedTiO2_pandas_format.csv
# C:\Users\nfinch\Desktop\lab_data_averages_pandas_format.csv
# C:\Users\nfinch\Desktop\mask_minors_noise.csv

fun_list.append(pysat.set_file_outpath)
arg_list.append([r"C:\Users\rbanderson\Documents\Projects\LIBS PDART\Output"])                                                                    # set_file_outpath
kw_list.append({})                                                                                                      # set_file_outpath

fun_list.append(pysat.get_data)
arg_list.append([r"C:\Users\rbanderson\Documents\Projects\LIBS PDART\Sample_Data\full_db_mars_corrected_dopedTiO2_pandas_format.csv", "known data"])          # get_data
kw_list.append({})                                                                                                      # get_data

fun_list.append(pysat.get_data)
arg_list.append([r"C:\Users\rbanderson\Documents\Projects\LIBS PDART\Sample_Data\lab_data_averages_pandas_format.csv", "unknown data"])                       # get_data
kw_list.append({})                                                                                                      # get_data

fun_list.append(pysat.do_interp)
arg_list.append(['unknown data','known data'])
kw_list.append({})                                                                                                      

fun_list.append(pysat.do_mask)
arg_list.append(['known data', r"C:\Users\rbanderson\Documents\Projects\LIBS PDART\Input\mask_minors_noise.csv"])                                       # do_mask
kw_list.append({})                                                                                                      # do_mask

fun_list.append(pysat.do_norm)
arg_list.append(['known data', [(0,350),(350,470),(470,1000)]])                                                         # do_norm
kw_list.append({})                                                                                                      # do_norm

fun_list.append(pysat.do_pca)
arg_list.append(['known data',5,'wvl'])
kw_list.append({})

fun_list.append(pysat.do_pca_ica_plot)
arg_list.append(['known data',1,2,'PCA_plot_SiO2.png'])
kw_list.append({'colorvar':('comp','SiO2'),'cmap':'viridis','method':'PCA'})

fun_list.append(pysat.do_strat_folds)
arg_list.append(['known data', 5, 2, ('comp', 'SiO2')])                                                                 # do_strat_folds
kw_list.append({})                                                                                                      # do_strat_folds

fun_list.append(pysat.do_regression_train)
arg_list.append(['known data', 'wvl', ('comp', 'SiO2'), 'PLS', {'n_components': 7, 'scale': False}, {}])                # do_regression_train
kw_list.append({})                                                                                                      # do_regression_train

fun_list.append(pysat.do_regression_predict)
arg_list.append(['known data', 'PLS', 'wvl'])                                                                           # do_regression_predict
kw_list.append({})                                                                                                      # do_regression_predict

fun_list.append(pysat.do_scatterplot)
arg_list.append(['known data', ('comp', 'SiO2'), ('meta', 'PLS_prediction'), 'PLS_SiO2_nc7.png'])                       # do_scatterplot
kw_list.append({'one_to_one': True})                                                                                    # do_scatterplot


for i in range(len(fun_list)):
    print(i)
    fun_list[i](*arg_list[i], **kw_list[i])
