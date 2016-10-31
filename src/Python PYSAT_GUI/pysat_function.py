from pysat.spectral.spectral_data import spectral_data
from pysat.regression import regression
from pysat.plotting.plots import scatterplot
import pandas as pd
from PYSAT_UI_MODULES.Error_ import error_print




class pysat_func(object):
    def __init__(self):
        self.data={} #initialize with an empty dict to hold data frames
        self.datakeys=[]
        self.models={}
        self.modelkeys=[]

        self.fun_list = []
        self.arg_list = []
        self.kw_list = []

    def getDataKeys(self):
        return self.datakeys

    def getModelKeys(self):
        return self.modelkeys

    def getData(self):
        return self.data

    def getModels(self):
        return self.models

    def set_file_outpath(self, outpath):
        try:
            self.outpath = outpath
            print("Output path folder has been set")
        except Exception as e:
            error_print(e)

    def get_data(self, filename, keyname):
        try:
            print('Loading data file: ' + str(filename))
            self.data[keyname] = spectral_data(pd.read_csv(filename, header=[0, 1]))
            self.datakeys.append(keyname)

        except Exception as e:
            error_print('Problem reading data: {}'.format(e))

    def do_mask(self, datakey, maskfile):
        try:
            self.data[datakey].mask(maskfile)
            print("Mask applied")
        except Exception as e:
            error_print(e)

    def submodel_ranges(self, datakey, ranges):
        print("{}".format(ranges))
        try:
            self.data[datakey].norm(ranges)
            print("Normalization has been applied to the ranges: " + str(ranges))
        except Exception as e:
            error_print(e)

    def do_strat_folds(self,datakey,nfolds,testfold,colname):
        self.data[datakey].stratified_folds(nfolds=nfolds,sortby=colname)
        
        self.data[datakey+'-Train']=self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
        self.data[datakey+'-Test']=self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
        self.datakeys=self.data.keys()
        
        
        print(self.data.keys())
        print(self.data[datakey+'-Test'].df.index.shape)
        print(self.data[datakey+'-Train'].df.index.shape)

    def do_regression_train(self, datakey, xvars, yvars, method, params, ransacparams):
        try:
            self.models[method] = regression.regression([method], [params], i=0, ransacparams=[ransacparams])
            self.modelkeys.append(method)
            self.models[method].fit(self.data[datakey].df[xvars], self.data[datakey].df[yvars])
            self.predictname = ('meta', method + '_prediction')
        except Exception as e:
            error_print(e)

    def do_regression_predict(self, datakey, modelkey, xvars):
        try:
            prediction = self.models[modelkey].predict(self.data[datakey].df[xvars])
            self.data[datakey].df[self.predictname] = prediction
        except Exception as e:
            error_print(e)

    def do_scatterplot(self, datakey,                                 # This
                       xvar, yvar,                                    # is
                       figname, xrange=None,                          # really
                       yrange=None, xtitle='Reference (wt.%)',        # really
                       ytitle='Prediction (wt.%)', title=None,        # really
                       lbls=None, one_to_one=False,                   # really
                       dpi=1000, colors=None,                         # really
                       annot_mask=None, alpha=0.4,                    # really
                       cmap=None, colortitle=''):                     # long

        x = [self.data[datakey].df[xvar]]
        y = [self.data[datakey].df[yvar]]
        scatterplot(x, y, self.outpath, figname, xrange=xrange, yrange=yrange, xtitle=xtitle, ytitle=ytitle, title=title,
                    lbls=lbls, one_to_one=one_to_one, dpi=dpi, colors=colors, annot_mask=annot_mask, alpha=alpha, cmap=cmap,
                    colortitle=colortitle)