from pysat.spectral.spectral_data import spectral_data
from pysat.regression.pls_sm import pls_sm
import pandas as pd

class pysat_function(object):
    def __init__(self, outpath, db, unknowndata, maskfile):
        self.outpath = outpath
        self.db = db
        self.unknowndata = unknowndata
        self.maskfile = maskfile

    def set_spectral(self, data):
        data = pd.read_csv(self.db, header=[0, 1])
        data = spectral_data(data)
        unknown_data = pd.read_csv(unknowndatacsv, header=[0, 1])
        unknown_data = spectral_data(unknown_data)
        unknown_data.interp(data.df['wvl'].columns)

        data.mask(self.maskfile)
        unknown_data.mask(self.maskfile)
        return data

    def interp(self, data):



    def get_ranges(self, data. range):
        ranges1 = range

        data.norm(ranges1)
        unknown_data = unknown_data
        unknown_data.norm(ranges1)
        return data

    def get_element_name(self,el, nfolds_test, testfold_test):
        el = 'SiO2'
        nfolds_test = 6
        testfold_test = 4


