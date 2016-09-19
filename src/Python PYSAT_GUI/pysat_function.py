
from pysat.spectral.spectral_data import spectral_data
from pysat.regression.pls_sm import pls_sm
import pandas as pd

class pysat_func(object):
    # Thus make sure that you have if's for all instances in functions where unknown_data doesn't exist.

    def set_files(self, **kwargs):
        for key, value in kwargs.items():
            if key == "outpath":
                self.outpath = value
            elif key == "db":
                self.db = value
            elif key == "unknowndatacsv":
                self.unknowndatacsv = value
            elif key == "maskfile":
                self.maskfile = value

    def set_interp(self, data):
        # TODO interp should be it's ownn function
        self.unknown_data.interp(self.data.df['wvl'].columns)

    def get_range(self, data, ranges):
        pass

    def get_spectra(self):
        self.data = pd.read_csv(self.db, header=[0, 1])
        self.data = spectral_data(self.data)
        self.unknown_data = pd.read_csv(self.unknowndatacsv, header=[0, 1])
        self.unknown_data = spectral_data(self.unknown_data)
    
    def set_mask(self):
        pass

    def get_ranges(self, data, ranges):
        data.norm(ranges)
        unknown_data = self.unknown_data
        unknown_data.norm(ranges)
        return unknown_data

    def set_element_name(self, el):
        self.el = el

    def set_nfolds(self, nfolds_test):
        self.nfolds_test = nfolds_test

    def set_testfold_test(self, testfold_test):
        self.testfold_test = testfold_test

    def get_element_name(self):
        return self.el

    def get_nfolds(self):
        return self.nfolds_test

    def get_testfold_test(self):
        return self.testfold_test

    def set_compranges(self, data):
        """ Usage:         [[-20, 50], [30, 70], [60, 100], [0, 120]]
        :param data:
        :return:
        """

    def set_stratified(self, data1):
        data1.stratified_folds(nfolds=nfolds_test, sortby=('meta', el))
        self.data1_train = data1.rows_match(('meta', 'Folds'), [testfold_test], invert=True)
        self.data1_test = data1.rows_match(('meta', 'Folds'), [testfold_test])

    def get_number_components(self, ncs):
        # ncs = [7, 7, 5, 9]
        self.ncs = ncs
        
    def get_train_data(self, traindata):
        #traindata = [data1_train.df, data1_train.df, data1_train.df, data1_train.df]
        self.traindata = traindata
    
    def get_testdata(self, testdata):
        #testdata = [data1_test.df, data1_test.df, data1_test.df, data1_test.df]
        self.testdata = testdata
        
    def get_unkdata(self, unkdata):
        #unkdata = [unknown_data1.df, unknown_data1.df, unknown_data1.df, unknown_data1.df]
        self.unkdata = unkdata
        
    def set_sm(self, sm):
        self.sm = pls_sm()

    def get_sm_fit(self):
        self.sm.fit(self.traindata, self.compranges, self.ncs, self.el, figpath=self.outpath)
        self.sm.fit(self.traindata, self.compranges, self.ncs, self.el, self.outpath)
        self.predictions_train = self.sm.predict(self.traindata)
        self.predictions_test = self.sm.predict(self.testdata)
        self.blended_train = self.sm.do_blend(self.predictions_train, self.traindata[0]['meta'][self.el])
        self.blended_test = self.sm.do_blend(self.predictions_test)

    def get_plots(self):
        # ###################################################
        # # Create all the Plots in Outpath
        # ###################################################
        self.sm.final(testdata[0]['meta'][self.el],
            blended_test,
            el=self.el,
            xcol='Ref Comp Wt. %',
            ycol='Predicted Comp Wt. %',
            figpath=self.outpath)
