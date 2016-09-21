from pysat.spectral.spectral_data import spectral_data
from pysat.regression.pls_sm import pls_sm
import pandas as pd

class pysat_func(object):

    # Below are all your file setters. ======================================================

    def set_file_outpath(self, outpath):
        self.outpath = outpath

    def set_file_known_data(self, db):
        self.known_data = db

    def set_file_unknown_data(self, unknowndatacsv):
        self.unknown_data = unknowndatacsv

    def set_maskfile(self, maskfile):
        self.maskfile = maskfile

    # Below are all your file getters. ======================================================

    def get_outpath(self):
        return self.outpath

    def get_known_data(self):
        return self.known_data

    def get_unknown_data(self):
        return self.unknown_data

    def get_maskfile(self):
        return self.maskfile


    # Actual functions that do work =========================================================
    # Note functions double up because of known and unknown data, it is done this way because
    # I realized we want to keep things as private as possible between the two classes:
    # PYSAT_UI and PYSAT_FUNC
    # After working through everything, I realized doubling up on functions, is not the best
    # way forward. Instead we'll have to allow UI to have a little access to pysat_func.data
    # and pysat_func.unknowndata

    def set_interp(self, data_value_1, data_value_2):
        """
        Usage: set_interp(unknown_data, known_data)
        Technically speaking, the values can be set up any way you want.
        The only concern in the typing. Make sure both values are of type spectral_data
        """
        data_value_1.interp(data_value_2.df['wv1'].columns)


    def set_spectral_unknown(self):

    def set_spectral_known(self):

    def set_mask_known(self):

    def set_mask_unknown(self):