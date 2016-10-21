from pysat_function import pysat_func

# Initialize pysat for use


pysat = pysat_func()

# Build was successful

fun_list = []
arg_list=[]
kw_list=[]
arg_list.append([r"C:\Users\rbanderson\Documents\Projects\LIBS PDART\Output"])
arg_list.append([r"C:\Users\rbanderson\Documents\Projects\LIBS PDART\Sample_Data\full_db_mars_corrected_dopedTiO2_pandas_format.csv", "known data"])
arg_list.append(['known data',r"C:\Users\rbanderson\Documents\Projects\LIBS PDART\Input\mask_minors_noise.csv"])
arg_list.append(['known data',[(0, 1000)]])
arg_list.append(['known data',5,2,('meta','SiO2')])
arg_list.append(['known data','wvl',('meta','SiO2'),'PLS',{'n_components':7,'scale':False},{}])
arg_list.append(['known data','PLS','wvl'])
arg_list.append(['known data',('meta','SiO2'),('meta','PLS_prediction'),'PLS_SiO2_nc7.png'])

kw_list.append({})
kw_list.append({})
kw_list.append({})
kw_list.append({})
kw_list.append({})
kw_list.append({})
kw_list.append({})
kw_list.append({'one_to_one':True})

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
    fun_list[i](*arg_list[i],**kw_list[i])