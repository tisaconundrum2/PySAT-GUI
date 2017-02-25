from pysat.spectral.spectral_data import spectral_data
from pysat.regression import regression
from pysat.regression import cv
from pysat.plotting.plots import make_plot, pca_ica_plot
from pysat.regression import sm
import pandas as pd
from PYSAT_UI_MODULES.Error_ import error_print
from PYSAT_UI_MODULES.del_layout_ import *
from PyQt4.QtCore import QThread
from PyQt4 import QtCore
import numpy as np


class Node:
    nodeCount = 0

    def __init__(self, fun_list=None, arg_data=None, kw_data=None):
        self.fun_data = fun_list
        self.arg_data = arg_data
        self.kw_data = kw_data
        self.next = None
        self.UI_ID = Node.nodeCount
        Node.nodeCount += 1

    def setData(self, fun_data=None, arg_data=None, kw_data=None):
        if fun_data is not None:
            self.fun_data = fun_data
        if arg_data is not None:
            self.arg_data = arg_data
        if kw_data is not None:
            self.kw_data = kw_data

    def getData(self, fun_data=False, arg_data=False, kw_data=False):
        """
        Put True as a parameter in order to get specific Data.
        :param fun_data:
        :param arg_data:
        :param kw_data:
        :return:
        """
        if fun_data:
            return self.fun_data
        if arg_data:
            return self.arg_data
        if kw_data:
            return self.kw_data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def getID(self):
        return self.UI_ID


class List:
    def __init__(self):
        self.head = None

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def push(self, fun_data=None, arg_data=None, kw_data=None, UI_ID=None):  # push new data into proper place.
        if not self.amend(fun_data, arg_data, kw_data, UI_ID):
            pass

    def amend(self, fun_data=None, arg_data=None, kw_data=None, UI_ID=None):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getID() == UI_ID:
                found = True
                current.setData(fun_data, arg_data, kw_data)
            else:
                current = current.getNext()
        return found

    def pop(self, fun_data=False, arg_data=False, kw_data=False):
        current = self.head
        previous = None
        while current.getNext() is not None:
            previous = current
            current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            return current.getData(fun_data, arg_data, kw_data)

    def remove(self, UI_ID):
        """
            Remove an item in the List based on UI_ID

            :param UI_ID: UI ID for identifying Node with content

            :return False: if we do not find the Node
            """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getID() == UI_ID:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def display(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()


class pysat_func(QThread):
    taskFinished = QtCore.pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
        self.leftOff = 0
        self.data = {}  # initialize with an empty dict to hold data frames
        self.datakeys = []
        self.models = {}
        self.modelkeys = []
        self.model_xvars = {}
        self.model_yvars = {}
        self.figs = {}
        self.fun_list = List()
        self.arg_list = List()
        self.kw_list = List()
        self.greyed_modules = List()

    """
    Getter and setter functions below
    """

    def set_fun_list(self, fun, index):
        self.fun_list.push(fun, index)
        print("")

    def set_arg_list(self, args, index):
        self.arg_list.push(args, index)

    def set_kw_list(self, kws, index):
        self.kw_list.push(kws, index)

    def set_greyed_modules(self, modules, index):
        self.greyed_modules.push(modules, index)

    """
    Work functions below
    """

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
            pass
        except Exception as e:
            error_print('Problem reading data: {}'.format(e))

    def removenull(self, datakey, colname):
        try:
            print(self.data[datakey].df.shape)
            self.data[datakey] = spectral_data(self.data[datakey].df.ix[-self.data[datakey].df[colname].isnull()])
            print(self.data[datakey].df.shape)

        except Exception as e:
            error_print(e)

    def do_mask(self, datakey, maskfile):
        try:
            self.data[datakey].mask(maskfile)
            print("Mask applied")
        except Exception as e:
            error_print(e)

    def do_interp(self, datakey_to_interp, datakey_ref):
        print(self.data[datakey_ref].df.columns.levels[0])
        try:
            self.data[datakey_to_interp].interp(self.data[datakey_ref].df['wvl'].columns)
        except Exception as e:
            error_print(e)

    def do_pca(self, datakey, nc, col, load_fit):
        print(self.data[datakey].df.columns.levels[0])
        try:
            self.data[datakey].pca(col, nc=nc, load_fit=load_fit)
        except Exception as e:
            error_print(e)

    def do_ica(self, datakey, nc, col, load_fit=None):
        try:
            self.data[datakey].ica(col, nc=nc, load_fit=load_fit)
        except Exception as e:
            error_print(e)

    def do_ica_jade(self, datakey, nc, col, load_fit=None, corrcols=None):
        try:
            self.data[datakey].ica_jade(col, nc=nc, load_fit=load_fit, corrcols=corrcols)
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

    def do_strat_folds(self, datakey, nfolds, testfold, colname):
        self.data[datakey].stratified_folds(nfolds=nfolds, sortby=colname)

        self.data[datakey + '-Train'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold], invert=True)
        self.data[datakey + '-Test'] = self.data[datakey].rows_match(('meta', 'Folds'), [testfold])
        self.datakeys = self.data.keys()

        print(self.data.keys())
        print(self.data[datakey + '-Test'].df.index.shape)
        print(self.data[datakey + '-Train'].df.index.shape)

    def do_regression_train(self, datakey, xvars, yvars, yrange, method, params, ransacparams, modelkey=None):
        try:
            if modelkey is None:
                modelkey = method + '-' + str(yvars) + ' (' + str(yrange[0]) + '-' + str(yrange([1]) + ') ')
            self.models[modelkey] = regression.regression([method], [yrange], [params], i=0,
                                                          ransacparams=[ransacparams])
            self.modelkeys.append(modelkey)

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
            print('foo')
        except Exception as e:
            error_print(e)

    def do_cv_train(self, datakey, xvars, yvars, method, params):

        try:
            cv_obj = cv.cv(params)
            self.data[datakey].df, self.cv_results = cv_obj.do_cv(self.data[datakey].df, xcols=xvars, ycol=yvars)
            self.data['CV Results'] = self.cv_results

        except Exception as e:
            error_print(e)

    def do_regression_predict(self, datakey, modelkey, predictname):
        try:
            prediction = self.models[modelkey].predict(self.data[datakey].df[self.model_xvars[modelkey]])
            self.data[datakey].df[predictname] = prediction
            pass
        except Exception as e:
            error_print(e)

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
            self.data[datakey].df[submodel_names[i] + '-Predict'] = j
        self.data[datakey].df['Blended-Predict (' + str(sm_obj.blendranges) + ')'] = predictions_blended

    def do_plot(self, datakey,
                xvar, yvar,
                figfile=None, xrange=None,
                yrange=None, xtitle='Reference (wt.%)',
                ytitle='Prediction (wt.%)', title=None,
                lbl=None, one_to_one=False,
                dpi=1000, color=None,
                annot_mask=None,
                cmap=None, colortitle='', figname=None, masklabel='',
                marker='o', linestyle='None'
                ):

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
            # Alpha is missing, fix this!
            outpath = self.outpath
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig)
        except Exception as e:
            error_print(e)
            # dealing with the a possibly missing outpath
            outpath = './'
            self.figs[figname] = make_plot(x, y, outpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                           ytitle=ytitle, title=title,
                                           lbl=lbl, one_to_one=one_to_one, dpi=dpi, color=color,
                                           annot_mask=annot_mask, cmap=cmap,
                                           colortitle=colortitle, loadfig=loadfig)

    def do_pca_ica_plot(self, datakey,
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
            del self.pysat_ui.ui_list
        except:
            pass
        try:
            del_qwidget_(self.greyed_modules[-1])
        except:
            pass
        try:
            del self.greyed_modules[-1]
        except:
            pass
        try:
            del self.fun_list[-1]
        except:
            pass
        try:
            del self.kw_list[-1]
        except:
            pass
        try:
            del self.arg_list[-1]
        except:
            pass
        #################################################### Begin Printing out debugging information
        for i in range(0, len(self.fun_list)):
            print("fun_list: {}".format(self.fun_list[i]))
        print("")
        for i in range(0, len(self.arg_list)):
            print("arg_list: {}".format(self.arg_list[i]))
        print("")
        for i in range(0, len(self.kw_list)):
            print("kw_list: {}".format(self.kw_list[i]))
        print("")
        #################################################### Endof Printing out debugging information

    def run(self):
        # TODO this function will take all the enumerated functions and parameters and run them
        try:
            #################################################### Begin Printing out debugging information
            self.fun_list.display()
            print("")
            self.arg_list.display()
            print("")
            self.kw_list.display()

            #################################################### Endof Printing out debugging information

            # for i in range(self.leftOff, self.fun_list.size()):
            #     self.fun_list[i](*self.arg_list[i], **self.kw_list[i])
            #     self.greyed_modules[i].setDisabled(True)
            #     self.leftOff = i + 1
            self.taskFinished.emit()
        except Exception as e:
            error_print(e)
            self.taskFinished.emit()
