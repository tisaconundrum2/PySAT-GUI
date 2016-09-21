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

    def set_file_maskfile(self, maskfile):
        self.maskfile = maskfile

    # Below are all your file getters. ======================================================

    def get_file_outpath(self):
        return self.outpath

    def get_file_known_data(self):
        return self.known_data

    def get_file_unknown_data(self):
        return self.unknown_data

    def get_file_maskfile(self):
        return self.maskfile


    # Actual functions that do work =========================================================
    # Note functions double up because of known and unknown data, it is done this way because
    # I realized we want to keep things as private as possible between the two classes:
    # PYSAT_UI and PYSAT_FUNC
    # After working through everything, I realized doubling up on functions, is not the best
    # way forward. Instead we'll have to allow UI to have a little access to pysat_func.data
    # and pysat_func.unknowndata

    def set_spectral(self, data_base):
        """
        The user will choose from either database of unknowndatacsv or db
        this means usage will be either:
        k_data = set_spectral(pysat.get_file_known_data())
        u_data = set_spectral(pysat.get_file_unknown_data())
        :param data_base:
        :return:
        """
        data = pd.read_csv(data_base, header=[0, 1])
        return spectral_data(data)

    def set_interp(self, data_value_1, data_value_2):
        """
        Usage:
        set_interp(u_data, k_data)
        Technically speaking, the values can be set up any way you want.
        The only concern in the typing. Make sure both values are of type spectral_data
        :param data_value_1
        :param data_value_2
        :return:
        """
        data_value_1.interp(data_value_2.df['wv1'].columns)

    def set_mask(self, data, maskfile):
        """
        Usage:
        set_mask(pysat.get_known_data(), pysat.get_maskfile())
        set_mask(pysat.get_unknown_data(), pysat.get_maskfile())
        :param data:
        :param maskfile:
        :return:
        """
        pass

    def get_range(self, data, ranges):
        """
        Usage:
        pysat.get_ranges(k_data, [(0, 1000)])
        pysat.get_ranges(u_data, [(0, 1000)])
        :param data:
        :param ranges:
        :return:
        """
        data.norm(ranges)