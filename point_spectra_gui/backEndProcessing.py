import traceback

import numpy as np
# from plio import io_ccam_pds
import pandas as pd
import subprocess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from pysat.fileio import io_ccam_pds
from pysat.plotting.plots import make_plot, pca_ica_plot
from pysat.regression import cv
from pysat.regression import regression
from pysat.regression import sm
from pysat.spectral.spectral_data import spectral_data
from point_spectra_gui.ui_modules.Error_ import error_print
from point_spectra_gui.ui_modules.del_layout_ import *


class backEndProc(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.data = {}  # initialize with an empty dict to hold data frames
        self.datakeys = []
        self.models = {}
        self.modelkeys = []
        self.model_xvars = {}
        self.model_yvars = {}
        self.dim_reds = {}
        self.dim_red_keys = []
        self.figs = {}
        self._list = listOfModules()
        self.greyed_modules = []
        self.outpath = './'

    def do_remove_baseline(self, datakey, method, params):
        datakey_new = datakey + '-Baseline Removed-' + method + str(params)
        datakey_baseline = datakey + '-Baseline-' + method + str(params)
        self.datakeys.append(datakey_new)
        self.datakeys.append(datakey_baseline)
        self.data[datakey_new] = spectral_data(self.data[datakey].df.copy(deep=True))
        self.data[datakey_new].remove_baseline(method, segment=True, params=params)
        self.data[datakey_baseline] = spectral_data(self.data[datakey_new].df_baseline)

    def do_dim_red(self, datakey, method, params, method_kws={}, col='wvl', load_fit=None, dim_red_key=None):
        try:
            if method == 'PCA' or method == 'ICA':
                self.dim_reds[dim_red_key] = self.data[datakey].dim_red(col, method, params, method_kws,
                                                                        load_fit=load_fit)
                self.dim_red_keys.append(dim_red_key)
            elif method == 'ICA-JADE':
                pass
                self.dim_reds[dim_red_key] = self.data[datakey].ica_jade(col)
        except Exception as e:
            print(e)

    def do_pca(self, datakey, nc, col, load_fit=None):
        print(self.data[datakey].df.columns.levels[0])
        try:
            self.data[datakey].pca(col, nc=nc, load_fit=load_fit)
        except Exception as e:
            print(e)

    def do_ica(self, datakey, nc, col, load_fit=None):
        try:
            self.data[datakey].ica(col, nc=nc, load_fit=load_fit)
        except Exception as e:
            print(e)

    def do_ica_jade(self, datakey, nc, col, load_fit=None, corrcols=None):
        try:
            self.data[datakey].ica_jade(col, nc=nc, load_fit=load_fit, corrcols=corrcols)
        except Exception as e:
            print(e)

    def do_norm(self, datakey, ranges, col_var='wvl'):
        print("{}".format(ranges))
        try:
            print(self.data[datakey].df.columns.levels[0])
            self.data[datakey].norm(ranges, col_var=col_var)
            print(self.data[datakey].df.columns.levels[0])
            print("Normalization has been applied to the ranges: " + str(ranges))
        except Exception as e:
            print(e)

    def do_cal_tran(self,data_transform,data_ref,col_match_ref,col_match_transform,method):
        self.data[data_transform].cal_tran(self.data[data_ref].df,col_match_ref,col_match_transform,method)

    def do_strat_folds(self, datakey, nfolds, testfold, colname):
        self.data[datakey].stratified_folds(nfolds=nfolds, sortby=colname)

        self.data[datakey + '-Train'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
        self.data[datakey + '-Test'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
        self.datakeys = self.data.keys()

        print(self.data.keys())
        print(self.data[datakey + '-Test'].df.index.shape)
        print(self.data[datakey + '-Train'].df.index.shape)

    # TODO: This module needs to be looked at. It's parameters are not correct
    def do_regression_train(self, datakey, xvars, yvars, yrange, method, params, ransacparams, modelkey=None,
                            update=False, append=False):
        try:
            if modelkey is None:
                modelkey = method + '-' + str(yvars) + ' (' + str(yrange[0]) + '-' + str(yrange([1]) + ') ')

            self.models[modelkey] = regression.regression([method], [yrange], [params], i=0,
                                                          ransacparams=[ransacparams])
            if not append:
                self.modelkeys.append(modelkey)
            else:
                self.modelkeys[-1] = modelkey
            if not update:
                x = self.data[datakey].df[xvars]
                y = self.data[datakey].df[yvars]
                x = np.array(x)
                y = np.array(y)
                ymask = np.squeeze((y > yrange[0]) & (y < yrange[1]))
                y = y[ymask]
                x = x[ymask, :]
                self.models[modelkey].fit(x, y)
                self.model_xvars[modelkey] = xvars
                self.model_yvars[modelkey] = yvars
                try:
                    coef = np.squeeze(self.models[modelkey].model.coef_)
                    coef = pd.DataFrame(coef)
                    coef.index = pd.MultiIndex.from_tuples(self.data[datakey].df[xvars].columns.values)
                    coef = coef.T
                    coef[('meta', 'Model')] = modelkey

                    try:
                        self.data['Model Coefficients'] = spectral_data(
                            pd.concat([self.data['Model Coefficients'].df, coef]))
                    except:
                        self.data['Model Coefficients'] = spectral_data(coef)
                        self.datakeys.append('Model Coefficients')
                except:
                    pass

        except Exception as e:
            print(e)

    def do_cv_train(self, datakey, xvars, yvars, yrange, method, params):

        try:
            y = np.array(self.data[datakey].df[yvars])
            match = np.squeeze((y > yrange[0]) & (y < yrange[1]))
            data_for_cv = spectral_data(self.data[datakey].df.ix[match])
            cv_obj = cv.cv(params)
            self.data[datakey].df, self.cv_results = cv_obj.do_cv(data_for_cv.df, xcols=xvars, ycol=yvars,
                                                                  yrange=yrange, method=method)
            self.data['CV Results'] = self.cv_results
        except Exception as e:
            print(e)

    def do_regression_predict(self, datakey, modelkey, predictname):
        try:
            prediction = self.models[modelkey].predict(self.data[datakey].df[self.model_xvars[modelkey]])
            self.data[datakey].df[predictname] = prediction
            pass
        except Exception as e:
            print(e)

    def do_submodel_predict(self, datakey, submodel_names, modelranges, trueval_data):
        # Check if reference data name has been provided
        # if so, get reference data values
        if trueval_data is not None:
            truevals = self.data[trueval_data].df[self.model_yvars[submodel_names[0]]]
            x_ref = []
        else:
            truevals = None

        # step through the submodel names and get the actual models and the x data
        x = []
        submodels = []
        for i in submodel_names:
            x.append(self.data[datakey].df[self.model_xvars[i]])
            submodels.append(self.models[i])
            if trueval_data is not None:
                x_ref.append(self.data[trueval_data].df[self.model_xvars[i]])

        # create the submodel object
        sm_obj = sm.sm(modelranges, submodels)

        # optimize blending if reference data is provided (otherwise, modelranges will be used as blending ranges)
        if truevals is not None:
            ref_predictions = sm_obj.predict(x_ref)
            ref_predictions_blended = sm_obj.do_blend(ref_predictions, truevals=truevals)

        # get predictions for each submodel separately
        predictions = sm_obj.predict(x)

        # blend the predictions together
        predictions_blended = sm_obj.do_blend(predictions)

        # save the individual and blended predictions
        for i, j in enumerate(predictions):
            self.data[datakey].df[('predict', submodel_names[i] + '-Predict')] = j
        self.data[datakey].df[('predict', 'Blended-Predict')] = predictions_blended
        pass

    def do_plot(self, datakey,
                xvar, yvar,
                figfile=None, xrange=None,
                yrange=None, xtitle='Reference (wt.%)',
                ytitle='Prediction (wt.%)', title=None,
                lbl=None, one_to_one=False,
                dpi=1000, color=None,
                annot_mask=None,
                cmap=None, colortitle='', figname=None, masklabel='',
                marker='o', linestyle='None', alpha=0.5
                ):

        try:
            if self.data[datakey].df.columns.nlevels == 2:
                vars_level0 = self.data[datakey].df.columns.get_level_values(0)
                vars_level1 = self.data[datakey].df.columns.get_level_values(1)
                vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
                vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
                xvar = (vars_level0[vars_level1.index(xvar)], xvar)
                yvar = (vars_level0[vars_level1.index(yvar)], yvar)
        except:
            pass

        try:
            x = self.data[datakey].df[xvar]
            y = self.data[datakey].df[yvar]
        except:
            x = self.data[datakey][xvar]
            y = self.data[datakey][yvar]
        try:
            loadfig = self.figs[figname]
        except:
            loadfig = None
            # outpath=self.outpath
        try:
            outpath = self.outpath
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle)
        except Exception as e:
            print(e)
            # dealing with the a possibly missing outpath
            outpath = './'
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle)

    def do_plot_spect(self, datakey,
                      row,
                      xcol='wvl',
                      figfile=None, xrange=None,
                      yrange=None, xtitle='Wavelength (nm)',
                      ytitle=None, title=None,
                      lbl=None, one_to_one=False,
                      dpi=1000, color=None,
                      annot_mask=None,
                      cmap=None, colortitle='', figname=None, masklabel='',
                      marker=None, linestyle='-', col=None, alpha=0.5, linewidth=1.0):

        self.data[datakey].enumerate_duplicates(col)
        data = self.data[datakey].df

        y = np.squeeze(np.array(data.loc[data[('meta', col)].isin([row])][xcol].T))
        x = np.array(data[xcol].columns.values)
        if linestyle == 'None':
            marker = 'o'
        try:
            loadfig = self.figs[figname]
        except:
            loadfig = None

        try:
            outpath = self.outpath
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle,
                                           linewidth=linewidth)

        except Exception as e:
            print(e)
            # dealing with the a possibly missing outpath
            outpath = './'
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle)

    def do_plot_dim_red(self, datakey,
                        x_component,
                        y_component,
                        figfile,
                        colorvar=None,
                        cmap='viridis',
                        method='PCA'
                        ):
        pca_ica_plot(self.data[datakey], x_component, y_component, colorvar=colorvar, cmap=cmap, method=method,
                     figpath=self.outpath, figfile=figfile)

    def __del__(self):
        self.wait()

    def del_layout(self):
        # Deleting a whole lotta lists... >_<
        try:
            del_qwidget_(self.greyed_modules[-1])
            del self.greyed_modules[-1]
            self._list.del_module()
        except:
            error_print("Cannot delete")

    def run(self):
        # TODO this function will take all the enumerated functions and parameters and run them
        try:
            for i in range(len(self.greyed_modules)):
                r_list = self._list.pull()
                print(r_list)
                getattr(self, r_list[2])(*r_list[3], **r_list[4])  # TODO add comment about who is who
                self.greyed_modules[0].setDisabled(True)
                del self.greyed_modules[0]
            self.taskFinished.emit()
        except Exception as e:
            print(e)
            self.taskFinished.emit()
