from pysat.spectral.spectral_data import spectral_data
from pysat.regression.pls_sm import pls_sm
import pandas as pd
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import QThread


class pysat_func(QThread):
    # Thus make sure that you have if's for all instances in functions where unknown_data doesn't exist.
    def __init__(self):
        self.data={} #initialize with an empty dict to hold data frames
        self.datakeys=[]


    """
    Get all files
    """
    def set_file_outpath(self, outpath):
        try:
            self.outpath = outpath
            print("Output path folder has been set")
        except Exception as e:
            error_print(e)
    def set_file_maskfile(self, maskfile):
        try:
            self.maskfile = maskfile
            print("Masking file has been added")
        except Exception as e:
            error_print(e)

    def get_data(self,filename,keyname):
        try:
            print('Loading data file: '+str(filename))
            self.data[keyname]=spectral_data(pd.read_csv(filename,header=[0,1]))
            self.datakeys.append(keyname)

        except Exception as e:
            error_print('Problem reading data: {}'.format(e))
            
    """
    Getter and Setter functions
    """
    def get_spectra(self):
        try:
            print("Running Spectral on data set")
            self.data = pd.read_csv(self.db, header=[0, 1])
            self.data = spectral_data(self.data)
            self.unknown_data = pd.read_csv(self.unknowndatacsv, header=[0, 1])
            self.unknown_data = spectral_data(self.unknown_data)
            print("Spectral analysis has completed")
        except Exception as e:
            error_print("I am missing some files please fix: {}".format(e))

    def set_interp(self):
        # TODO interp should be it's ownn function
        try:
            self.unknown_data.interp(self.data.df['wvl'].columns)
            print("Interpolation has been applied")
        except Exception as e:
            error_print(e)

    def set_mask(self):
        try:
            self.data.mask(self.maskfile)
            self.unknown_data.mask(self.maskfile)
            print("Masking has been applied")
        except Exception as e:
            error_print(e)

    def get_ranges(self, ranges):
        print("{}".format(ranges))
        try:
            self.data.norm(ranges)
            self.unknown_data.norm(ranges)
            print("{}".format(ranges))
            print("Ranges have been applied")
        except Exception as e:
            error_print(e)

    def set_element_name(self, el):
        try:
            self.el = el
            print("{}".format(el))
            print("Element name for y variable has been set")
        except Exception as e:
            error_print(e)

    def set_nfolds(self, nfolds_test):
        try:
            self.nfolds_test = nfolds_test
            print("{}".format(nfolds_test))
            print("N folds has been applied")
        except Exception as e:
            error_print(e)

    def set_testfold(self, testfold_test):
        try:
            self.testfold_test = testfold_test
            print("{}".format(testfold_test))
            print("Test folds has been applied")
        except Exception as e:
            error_print(e)

    def set_nfolds(self):
        try:
            return self.nfolds_test
        except Exception as e:
            error_print(e)

    def do_strat_folds(self,datakey=None,nfolds=None,testfold=None,colname=None):
        try:
            self.data[datakey].stratified_folds(nfolds=nfolds,sortby=colname)
            self.data[datakey+'-Train']=self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
            self.data[datakey+'-Test']=self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
            print(self.data.keys())
            print(self.data[datakey+'-Test'].df.index.shape)
            print(self.data[datakey+'-Train'].df.index.shape)
        except Exception as e:
            error_print(e)

        
    
    def set_testfold(self):
        try:
            return self.testfold_test
        except Exception as e:
            error_print(e)

    def set_compranges(self, compranges):
        try:
            self.compranges = compranges
            print("{}".format(compranges))
            print("Submodel ranges has been applied")
        except Exception as e:
            error_print(e)

    def set_stratified(self):
        try:
            print("Beginning stratification of data")
            self.data.stratified_folds(nfolds=self.nfolds_test, sortby=('meta', self.el))
            self.data1_train = self.data.rows_match(('meta', 'Folds'), [self.testfold_test], invert=True)
            self.data1_test = self.data.rows_match(('meta', 'Folds'), [self.testfold_test])
            print("Finishing up on stratification")
        except Exception as e:
            error_print(e)

    def get_number_components(self, ncs):
        # ncs = [7, 7, 5, 9]
        try:
            self.ncs = ncs
            print("{}".format(ncs))
            print("Applying components")
        except Exception as e:
            error_print(e)


    def set_sm(self):
        self.sm = pls_sm()

    def get_sm_fit(self):
        print("Beginning SM fit")
        self.sm.fit(self.traindata, self.compranges, self.ncs, self.el, figpath=self.outpath)
        self.predictions_train = self.sm.predict(self.traindata)
        self.predictions_test = self.sm.predict(self.testdata)
        self.blended_train = self.sm.do_blend(self.predictions_train, self.traindata[0]['meta'][self.el])
        self.blended_test = self.sm.do_blend(self.predictions_test)
        print("Finishing up...")

    def get_plots(self):
        print("Now outputting plots to output folder")
        self.sm.final(self.testdata[0]['meta'][self.el],
                  self.blended_test,
                  el=self.el,
                  xcol='Ref Comp Wt. %',
                  ycol='Predicted Comp Wt. %',
                  figpath=self.outpath)
        print("All finished")


def error_print(message):
    """
    Warning Message Box
    """
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

