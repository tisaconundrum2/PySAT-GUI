from pysat.spectral.spectral_data import spectral_data
from pysat.regression import regression
from pysat.plotting.plots import scatterplot,pca_ica_plot
import pandas as pd
from PyQt4.QtGui import QMessageBox



class pysat_func(object):
    def __init__(self):
        self.data={} #initialize with an empty dict to hold data frames
        self.datakeys=[]
        self.models={}
        self.modelkeys=[]
        self.addFunc = []
        self.addPara = []
        self.figs={}
        self.fignames=[]

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
            
    def do_interp(self,datakey_to_interp,datakey_ref):
        print(self.data[datakey_ref].df.columns.levels[0])
        try:
            self.data[datakey_to_interp].interp(self.data[datakey_ref].df['wvl'].columns)
        except Exception as e:
            error_print(e)

    def do_pca(self,datakey,nc,col,load_fit=None):
        print(self.data[datakey].df.columns.levels[0])
        try:
            self.data[datakey].pca(col,nc=nc,load_fit=load_fit)
        except Exception as e:
            error_print(e)
    def do_ica(self,datakey,nc,col,load_fit=None):
        try:
            self.data[datakey].ica(col,nc=nc,load_fit=load_fit)
        except Exception as e:
            error_print(e)
    def do_ica_jade(self,datakey,nc,col,load_fit=None,corrcols=None):
        try:
            self.data[datakey].ica_jade(col,nc=nc,load_fit=load_fit,corrcols=corrcols)
        except Exception as e:
            error_print(e)
            
    def do_norm(self, datakey, ranges):
        print("{}".format(ranges))
        try:
            print(self.data[datakey].df.columns.levels[0])            
            self.data[datakey].norm(ranges)
            print(self.data[datakey].df.columns.levels[0])
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
            
        except Exception as e:
            error_print(e)

    def do_regression_predict(self, datakey, modelkey, xvars,predictname):
        try:
            prediction = self.models[modelkey].predict(self.data[datakey].df[xvars])
            self.data[datakey].df[predictname] = prediction
        except Exception as e:
            error_print(e)

    def do_scatterplot(self, datakey,                                 # This
                       xvar, yvar,                                    # is
                       figfile=None, xrange=None,                          # really
                       yrange=None, xtitle='Reference (wt.%)',        # really
                       ytitle='Prediction (wt.%)', title=None,        # really
                       lbls=None, one_to_one=False,                   # really
                       dpi=1000, colors=None,                         # really
                       annot_mask=None, alpha=0.4,                    # really
                       cmap=None, colortitle='',figname=None):                     # long

        x = [self.data[datakey].df[xvar]]
        y = [self.data[datakey].df[yvar]]
        try:
            loadfig=self.figs[figname]
        except:
            loadfig=None

        self.figs[figname]=scatterplot(x, y, self.outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle, ytitle=ytitle, title=title,
                    lbls=lbls, one_to_one=one_to_one, dpi=dpi, colors=colors, annot_mask=annot_mask, alpha=alpha, cmap=cmap,
                    colortitle=colortitle,loadfig=loadfig)
                    
                    
                    
    def do_pca_ica_plot(self,datakey,x_component,y_component,figfile,colorvar=None,cmap='viridis',method='PCA'):
        pca_ica_plot(self.data[datakey],x_component,y_component,colorvar=colorvar,cmap=cmap,method=method,figpath=self.outpath,figfile=figfile)
        

def error_print(message):
    print(message)
    try:
        """
        Warning Message Box
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    except:
        pass