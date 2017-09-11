from PyQt5 import QtWidgets

from point_spectra_gui.functions.regressionMethods import *
from point_spectra_gui.ui.CrossValidation import Ui_Form
from point_spectra_gui.util import delete
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        self.regressionMethods()
        self.connectWidgets()

    def get_widget(self):
        return self.regression

    def make_regression_widget(self, alg, params=None):
        self.algorithm_list = ['Choose an algorithm',  # 0
                               'PLS',  # 1
                               'GP',  # 2
                               'OLS',  # 3
                               'OMP',  # 4
                               'Lasso',  # 5
                               'Elastic Net',  # 6
                               'Ridge',  # 7
                               'Bayesian Ridge',  # 8
                               'ARD',  # 9
                               'LARS',  # 10
                               'Lasso LARS',  # 11
                               'SVR',  # 12
                               'KRR',  # 13
                               'More to come...']
        print(alg)

        # if alg == self.algorithm_list[1]:
        #
        #
        # if alg == self.algorithm_list[2]:
        #
        #
        # if alg == self.algorithm_list[3]:
        #
        #
        #     if params is not None:
        #         self.ols.fitInterceptCheckBox.setChecked(params['fit_intercept'])
        #
        # if alg == self.algorithm_list[4]:
        #
        #
        #     if params is not None:
        #         self.omp.fitInterceptCheckBox.setChecked(params['fit_intercept'])
        #         self.omp.optimizeWCrossValidationCheckBox.setChecked(params['CV'])
        #         self.omp.numOfNonZeroCoeffsSpinBox.setValue(params['n_nonzero_coefs'])
        #
        # if alg == self.algorithm_list[5]:
        #
        #
        # if alg == self.algorithm_list[6]:
        #
        #
        # if alg == self.algorithm_list[7]:
        #
        #
        # if alg == self.algorithm_list[8]:
        #
        #
        # if alg == self.algorithm_list[9]:
        #
        #
        # if alg == self.algorithm_list[10]:
        #
        #
        # if alg == self.algorithm_list[11]:
        #
        #
        # if alg == self.algorithm_list[12]:
        #
        #
        # if alg == self.algorithm_list[13]:


    def connectWidgets(self):
        self.regression_alg_choices.currentIndexChanged.connect(
            lambda: self.make_regression_widget(self.regression_alg_choices.currentText()))  #
        self.regression_choosedata.activated[int].connect(
            lambda: self.changeComboListVars(self.regression_choosey, self.yvar_choices()))
        self.regression_choosedata.activated[int].connect(
            lambda: self.changeComboListVars(self.regression_choosex, self.xvar_choices()))

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        method = self.regression_alg_choices.currentText()
        datakey = self.regression_choosedata.currentText()
        xvars = [str(x.text()) for x in self.regression_choosex.selectedItems()]
        yvars = [('comp', str(y.text())) for y in self.regression_choosey.selectedItems()]
        yrange = [self.yvarmin_spin.value(), self.yvarmax_spin.value()]
        params = {}
        ransacparams = {}
        kws = {}
        try:
            modelkey = method + ' - ' + str(yvars[0][-1]) + ' (' + str(yrange[0]) + '-' + str(yrange[1]) + ') '
        except:
            modelkey = method
        try:
            if method == 'OLS':
                params = {'fit_intercept': self.ols.fitInterceptCheckBox.isChecked()}
                modelkey = modelkey + str(params)
                print(params)

            if method == 'OMP':
                params = {'fit_intercept': self.omp.fitInterceptCheckBox.isChecked(),
                          'n_nonzero_coefs': self.omp.numOfNonZeroCoeffsSpinBox.value(),
                          'CV': self.omp.optimizeWCrossValidationCheckBox.isChecked()}
                self.omp.numOfNonZeroCoeffsSpinBox.setDisabled(params['CV'])
                modelkey = modelkey + str(params)
                print(params)

            if method == 'Lasso':
                params = {'alpha': self.lasso.alphaDoubleSpinBox.value(),
                          'fit_intercept': self.lasso.fitInterceptCheckBox.isChecked(),
                          'max_iter': int(self.lasso.maxNumOfIterationsSpinBox.value()),
                          'tol': self.lasso.toleranceDoubleSpinBox.value(),
                          'positive': self.lasso.forcePositiveCoefficientsCheckBox.isChecked(),
                          'selection': 'random',
                          'CV': self.lasso.optimizeWCrossValidaitonCheckBox.isChecked()}
                self.lasso.alphaDoubleSpinBox.setDisabled(params['CV'])
                print(params)

            if method == 'Elastic Net':
                p_attrib = {'False': False, 'True': True, 'Array-like': 'array-like'}
                r_attrib = {'None': None}
                try:
                    r_state = int(self.elastic_net.randomStateLineEdit.text())
                except:
                    r_state = r_attrib[self.elastic_net.randomStateLineEdit.text()]

                index = self.elastic_net.precomputeComboBox.currentIndex()
                precomputeComboBox = self.elastic_net.precomputeComboBox.itemText(index)

                params = {'alpha': self.elastic_net.alphaDoubleSpinBox.value(),
                          'l1_ratio': self.elastic_net.l1RatioDoubleSpinBox.value(),
                          'fit_intercept': self.elastic_net.fitInterceptCheckBox.isChecked(),
                          'normalize': self.elastic_net.normalizeCheckBox.isChecked(),
                          'precompute': p_attrib[precomputeComboBox],
                          'max_iter': int(self.elastic_net.maxNumOfIterationsSpinBox.value()),
                          'copy_X': self.elastic_net.copyXCheckBox.isChecked(),
                          'tol': self.elastic_net.toleranceDoubleSpinBox.value(),
                          'warm_start': self.elastic_net.warmStartCheckBox.isChecked(),
                          'positive': self.elastic_net.positiveCheckBox.isChecked(),
                          'selection': self.elastic_net.selectionLineEdit.text(),
                          'random_state': r_state,
                          'CV': self.elastic_net.crossValidateCheckBox.isChecked()}
                self.elastic_net.alphaDoubleSpinBox.setDisabled(params['CV'])
                self.elastic_net.l1RatioDoubleSpinBox.setDisabled(params['CV'])
                print(params)

            if method == 'Ridge':
                m_attrib = {'None': None}
                r_attrib = {'None': None}
                try:
                    m_state = int(self.ridge.maxNumOfIterationslineEdit.text())
                except:
                    m_state = m_attrib[self.ridge.maxNumOfIterationslineEdit.text()]
                try:
                    r_state = int(self.ridge.randomStateLineEdit.text())
                except:
                    r_state = r_attrib[self.elastic_net.randomStateLineEdit.text()]

                index = self.ridge.solverComboBox.currentIndex()
                params = {'alpha': self.ridge.alphaDoubleSpinBox.value(),
                          'copy_X': self.ridge.copyXCheckBox.isChecked(),
                          'fit_intercept': self.ridge.fitInterceptCheckBox.isChecked(),
                          'max_iter': m_state,
                          'normalize': self.ridge.normalizeCheckBox.isChecked(),
                          'solver': self.ridge.solverComboBox.itemText(index),
                          'tol': self.ridge.toleranceDoubleSpinBox.value(),
                          'random_state': r_state}

                print(params)

            if method == 'Bayesian Ridge':
                params = {'n_iter': self.br.numOfIterationsSpinBox.value(),
                          'tol': self.br.toleranceDoubleSpinBox.value(),
                          'alpha_1': self.br.alpha1DoubleSpinBox.value(),
                          'alpha_2': self.br.alpha2DoubleSpinBox.value(),
                          'lambda_1': self.br.lambdaDoubleSpinBox.value(),
                          'lambda_2': self.br.lambdaDoubleSpinBox.value(),
                          'compute_score': self.br.computerScoreCheckBox.isChecked(),
                          'fit_intercept': self.br.fitInterceptCheckBox.isChecked(),
                          'normalize': self.br.normalizeCheckBox.isChecked(),
                          'copy_X': self.br.copyXCheckBox.isChecked(),
                          'verbose': self.br.verboseCheckBox.isChecked()}
                print(params)

            if method == 'ARD':
                params = {'n_iter': self.ard.numOfIterationsSpinBox.value(),
                          'tol': self.ard.toleranceDoubleSpinBox.value(),
                          'alpha_1': self.ard.alpha1DoubleSpinBox.value(),
                          'alpha_2': self.ard.alpha2DoubleSpinBox.value(),
                          'lambda_1': self.ard.lambdaDoubleSpinBox.value(),
                          'lambda_2': self.ard.lambdaDoubleSpinBox.value(),
                          'compute_score': self.ard.computerScoreCheckBox.isChecked(),
                          'threshold_lambda': self.ard.thresholdLambdaSpinBox.value(),
                          'fit_intercept': self.ard.fitInterceptCheckBox.isChecked(),
                          'normalize': self.ard.normalizeCheckBox.isChecked(),
                          'copy_X': self.ard.copyXCheckBox.isChecked(),
                          'verbose': self.ard.verboseCheckBox.isChecked()}
                print(params)

            if method == 'LARS':
                params = {'n_nonzero_coefs': self.lars.numOfNonzeroCoeffsSpinBox.value(),
                          'fit_intercept': self.lars.fitInterceptCheckBox.isChecked(),
                          'positive': self.lars.positiveCheckBox.isChecked(),
                          'verbose': self.lars.verboseCheckBox.isChecked(),
                          'normalize': self.lars.normalizeCheckBox.isChecked(),
                          'precompute': self.lars.precomputeCheckBox.isChecked(),
                          'copy_X': self.lars.copyXCheckBox.isChecked(),
                          'eps': self.lars.epsDoubleSpinBox.value(),
                          'fit_path': self.lars.fitPathCheckBox.isChecked(),
                          'CV': self.lars.crossValidateCheckBox.isChecked()}
                self.lars.numOfNonzeroCoeffsSpinBox.setDisabled(params['CV'])
                self.lars.fitPathCheckBox.setDisabled(params['CV'])
                print(params)

            if method == 'Lasso LARS':
                p_attrib = {'Auto': 'auto', 'True': True, 'False': False, 'Array-like': 'array-like'}
                index = self.lassoLARS.precomputeComboBox.currentIndex()
                precomputeComboBox = self.lassoLARS.precomputeComboBox.itemText(index)

                params = {'alpha': self.lassoLARS.alphaDoubleSpinBox.value(),
                          'fit_intercept': self.lassoLARS.fitInterceptCheckBox.isChecked(),
                          'positive': self.lassoLARS.positiveCheckBox.isChecked(),
                          'verbose': self.lassoLARS.verboseCheckBox.isChecked(),
                          'normalize': self.lassoLARS.normalizeCheckBox.isChecked(),
                          'copy_X': self.lassoLARS.copyXCheckBox.isChecked(),
                          'precompute': p_attrib[precomputeComboBox],
                          'max_iter': int(self.lassoLARS.maxIterationsSpinBox.value()),
                          'eps': self.lassoLARS.epsDoubleSpinBox.value(),
                          'fit_path': self.lassoLARS.fitInterceptCheckBox.isChecked(),
                          'model': self.lassoLARS.modelComboBox.currentIndex()}
                print(params)

            if method == 'SVR':
                gamma_index = self.svr.gammaComboBox.currentIndex()
                kernel_index = self.svr.kernelComboBox.currentIndex()
                params = {'C': self.svr.cDoubleSpinBox.value(),
                          'epsilon': self.svr.epsilonDoubleSpinBox.value(),
                          'kernel': self.svr.kernelComboBox.itemText(kernel_index),
                          'degree': self.svr.degreeSpinBox.value(),
                          'gamma': self.svr.gammaComboBox.itemText(gamma_index),
                          'coef0': self.svr.coeff0DoubleSpinBox.value(),
                          'shrinking': self.svr.shrinkingCheckBox.isChecked(),
                          'tol': self.svr.toleranceDoubleSpinBox.value(),
                          'cache_size': self.svr.cacheSizeSpinBox.value(),
                          'verbose': self.svr.verboseCheckBox.isChecked(),
                          'max_iter': int(self.svr.maxIterationsSpinBox.value())}
                print(params)

            if method == 'KRR':
                k_attrib = {'None': None}
                params = {'alpha': self.krr.alphaSpinBox.value(),
                          'kernel': self.krr.kernelLineEdit.text(),
                          'gamma': self.krr.gammaLineEdit.text(),
                          'degree': self.krr.degreeDoubleSpinBox.value(),
                          'coef0': self.krr.coeff0DoubleSpinBox.value(),
                          'kernel_params': k_attrib[self.krr.kernelParametersLineEdit.text()]}
                print(params)

            if method == 'PLS':
                params = {'n_components': self.pls.numOfComponentsSpinBox.value(),
                          'scale': False}
                modelkey = modelkey + '(nc=' + str(params['n_components']) + ')'
                print(params)

            if method == 'GP':
                index = self.gp.chooseDimensionalityReductionMethodComboBox.currentIndex()
                params = {'reduce_dim': self.gp.chooseDimensionalityReductionMethodComboBox.itemText(index),
                          'n_components': self.gp.numOfComponentsSpinBox.value(),
                          'random_start': self.gp.numOfRandomStartsSpinBox.value(),
                          'theta0': self.gp.startingThetaDoubleSpinBox.value(),
                          'thetaL': self.gp.lowerBoundOnThetaDoubleSpinBox.value(),
                          'thetaU': self.gp.upperBoundOnThetaDoubleSpinBox.value()}

                modelkey = modelkey + str(params)
                print(params)

        except Exception as e:
            print(e)

    def yvar_choices(self):
        try:
            yvarchoices = self.data[self.regression_choosedata.currentText()].df['comp'].columns.values
            yvarchoices = [i for i in yvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            yvarchoices = ['No composition columns!']
        return yvarchoices

    def xvar_choices(self):
        try:
            xvarchoices = self.data[self.regression_choosedata.currentText()].df.columns.levels[0].values
            xvarchoices = [i for i in xvarchoices if not 'Unnamed' in i]  # remove unnamed columns from choices
        except:
            xvarchoices = ['No valid choices!']
        return xvarchoices

    def regressionMethods(self):
        self.alg = []
        list_forms = []
        list_forms.append(PLS)
        list_forms.append(GP)
        list_forms.append(OLS)
        list_forms.append(OMP)
        list_forms.append(Lasso)
        list_forms.append(ElasticNet)
        list_forms.append(Ridge)
        list_forms.append(BayesianRidge)
        list_forms.append(ARD)
        list_forms.append(LARS)
        list_forms.append(LassoLARS)
        list_forms.append(SVR)
        list_forms.append(KRR)
        for items in list_forms:
            self.alg.append(items.Ui_Form())
            self.alg[-1].setupUi(self.Form)
            self.algorithmLayout.addWidget(self.alg[-1].get_widget())
            self.alg[-1].setHidden(True)