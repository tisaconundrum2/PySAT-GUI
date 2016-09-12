from pysat.spectral.spectral_data import spectral_data
from pysat.regression.pls_sm import pls_sm
import pandas as pd

class pysat_func(object):
    def __init__(self, outpath, db, unknowndatacsv, maskfile):

        self.outpath = outpath
        self.db = db
        self.unknowndatacsv = unknowndatacsv
        self.maskfile = maskfile
        self.data


    def interp(self, data):
        pass

    def get_range(self, data, ranges):
        pass



    def getspectra(self):
        self.data = pd.read_csv(self.db, header=[0, 1])
        self.data = spectral_data(self.data)
        unknown_data = pd.read_csv(self.unknowndatacsv, header=[0, 1])
        unknown_data = spectral_data(unknown_data)
        unknown_data.interp(self.data.df['wvl'].columns)
        self.data.mask(self.maskfile)
        unknown_data.mask(self.maskfile)

###################################################
# Normalizing Data and getting Ranges
# range3: equivalent to norm3
# range1: equivalent to norm1
###################################################
    def get_ranges(self, data, ranges):
        data.norm(ranges)
        unknown_data = self.unknown_data
        unknown_data.norm(ranges)
        return unknown_data

###################################################
# nfolds: the number of folds to divide data into to extract an overall test set
# testfold: which fold to use as the overall test set
# nfolds_cv: Number of folds for CV
# testfold_cv: Which fold to use as the test set for cross validation
# Cross Validation
###################################################
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

###################################################
# Composition Ranges
# These are the composition ranges for the submodels
# nc: max number of components
###################################################
    def set_compranges(self, data):
        """ Usage:         [[-20, 50], [30, 70], [60, 100], [0, 120]]
        :param data:
        :return:
        """
###################################################
# remove a test set to be completely excluded from CV
# and used to assess the final blended model
###################################################
data1.stratified_folds(nfolds=nfolds_test, sortby=('meta', el))
data1_train = data1.rows_match(('meta', 'Folds'), [testfold_test], invert=True)
data1_test = data1.rows_match(('meta', 'Folds'), [testfold_test])

###################################################
# Create the models here in order: Low, Mid, High, Full
# The full model will be used as a references to determine which submodel is appropriate
# The Full model will be computed last
###################################################
ncs = [7, 7, 5, 9]
traindata = [data1_train.df, data1_train.df, data1_train.df, data1_train.df]
testdata = [data1_test.df, data1_test.df, data1_test.df, data1_test.df]
unkdata = [unknown_data1.df, unknown_data1.df, unknown_data1.df, unknown_data1.df]

sm = pls_sm()

sm.fit(traindata, compranges, ncs, el, figpath=outpath)

predictions_train = sm.predict(traindata)

predictions_test = sm.predict(testdata)

blended_train = sm.do_blend(predictions_train, traindata[0]['meta'][el])

blended_test = sm.do_blend(predictions_test)

###################################################
# Create all the Plots in Outpath
###################################################
sm.final(testdata[0]['meta'][el],
         blended_test,
         el=el,
         xcol='Ref Comp Wt. %',
         ycol='Predicted Comp Wt. %',
         figpath=outpath)
