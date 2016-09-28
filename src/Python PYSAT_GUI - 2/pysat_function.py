from pysat.spectral.spectral_data import spectral_data
from pysat.regression.pls_sm import pls_sm
import pandas as pd


class pysat_func():
    # Thus make sure that you have if's for all instances in functions where unknown_data doesn't exist.


    def set_file_outpath(self, outpath):
        self.outpath = outpath

    def set_file_knowndatacsv(self, db):
        self.db = db

    def set_file_unknowndatacsv(self, unknowndatacsv):
        self.unknowndatacsv = unknowndatacsv

    def set_file_maskfile(self, maskfile):
        self.maskfile = maskfile

    def get_spectra(self):
        self.data = pd.read_csv(self.db, header=[0, 1])
        self.data = spectral_data(self.data)
        self.unknown_data = pd.read_csv(self.unknowndatacsv, header=[0, 1])
        self.unknown_data = spectral_data(self.unknown_data)

    def set_interp(self):
        # TODO interp should be it's ownn function
        self.unknown_data.interp(self.data.df['wvl'].columns)

    def set_mask(self):
        self.data.mask(self.maskfile)
        self.unknown_data.mask(self.maskfile)

    def get_ranges(self, ranges):
        try:
            self.data.norm(ranges)
            self.unknown_data.norm(ranges)
        except Exception as e:
            print(e)


    def set_element_name(self, el):
        self.el = el

    def set_nfolds(self, nfolds_test):
        self.nfolds_test = nfolds_test

    def set_testfold_test(self, testfold_test):
        self.testfold_test = testfold_test

    def get_nfolds(self):
        return self.nfolds_test

    def get_testfold_test(self):
        return self.testfold_test

    def set_compranges(self, compranges):
        self.compranges = compranges

    def set_stratified(self):
        self.data.stratified_folds(nfolds=self.nfolds_test, sortby=('meta', self.el))
        self.data1_train = self.data.rows_match(('meta', 'Folds'), [self.testfold_test], invert=True)
        self.data1_test = self.data.rows_match(('meta', 'Folds'), [self.testfold_test])

    def get_number_components(self, ncs):
        # ncs = [7, 7, 5, 9]
        self.ncs = ncs

    def get_train_data(self):
        self.traindata = [self.data1_train.df, self.data1_train.df, self.data1_train.df, self.data1_train.df]

    def get_test_data(self):
        self.testdata = [self.data1_test.df, self.data1_test.df, self.data1_test.df, self.data1_test.df]

    def set_sm(self):
        self.sm = pls_sm()

    def get_sm_fit(self):
        self.sm.fit(self.traindata, self.compranges, self.ncs, self.el, figpath=self.outpath)
        self.predictions_train = self.sm.predict(self.traindata)
        self.predictions_test = self.sm.predict(self.testdata)
        self.blended_train = self.sm.do_blend(self.predictions_train, self.traindata[0]['meta'][self.el])
        self.blended_test = self.sm.do_blend(self.predictions_test)

    def get_plots(self):
        # ###################################################
        # # Create all the Plots in Outpath
        # ###################################################
        self.sm.final(self.testdata[0]['meta'][self.el],
                      self.blended_test,
                      el=self.el,
                      xcol='Ref Comp Wt. %',
                      ycol='Predicted Comp Wt. %',
                      figpath=self.outpath)
