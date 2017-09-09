from pysat.spectral.spectral_data import spectral_data

from point_spectra_gui.ui.BaselineRemoval import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        pass

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        params = self.getGuiParams()
        method = params['chooseAlgorithmComboBox']
        datakey = params['chooseDataComboBox']

        try:
            if method == 'ALS':
                methodParameters = {'asymmetry_param': self.br_widget.als_asym_spinbox.value(),
                                    'smoothness_param': self.br_widget.als_smooth_spinbox.value(),
                                    'max_iters': self.br_widget.als_iters_spinbox.value(),
                                    'conv_thresh': self.br_widget.als_conv_spinbox.value()}

            if method == 'Dietrich':
                self.br_widget.dietrich_half_win_spinbox.setValue(methodParameters['half_window'])
                self.br_widget.dietrich_erosions_spinbox.setValue(methodParameters['num_erosions'])

                methodParameters = {'half_window': self.br_widget.dietrich_half_win_spinbox.value(),
                                    'num_erosions': self.br_widget.dietrich_erosions_spinbox.value()}

            if method == 'Polyfit':
                methodParameters = {'poly_order': self.br_widget.polyfit_order_spinbox.value(),
                                    'num_stdev': self.br_widget.polyfit_nstdev_spinbox.value(),
                                    'max_iter': self.br_widget.polyfit_iter_spinbox.value()}

            if method == 'AirPLS':
                methodParameters = {'smoothness_param': self.br_widget.airpls_smoothness_spinbox.value(),
                                    'conv_thresh': self.br_widget.airpls_conv_spinbox.value(),
                                    'max_iters': self.br_widget.airpls_iter_spinbox.value()}

            if method == 'FABC':
                methodParameters = {'smoothness_param': self.br_widget.fabc_smoothness_spinbox.value(),
                                    'dilation_param': self.br_widget.fabc_dilation_spinbox.value()}

            if method == 'KK':
                methodParameters = {'top_width': self.br_widget.kk_top_width_spinbox.value(),
                                    'bottom_width': self.br_widget.kk_bottom_width_spinbox.value(),
                                    'tangent': self.br_widget.kk_tan_checkbox.isChecked(),
                                    'exponent': self.br_widget.kk_exp_spinbox.value()}

            if method == 'Mario':
                methodParameters = {'poly_order': self.br_widget.mario_order_spinbox.value(),
                                    'max_iters': self.br_widget.mario_iters_spinbox.value(),
                                    'tol': self.br_widget.mario_tol_spinbox.value()}

            if method == 'Median':
                methodParameters = {'window_size': self.br_widget.median_window_spinbox.value()}

            if method == 'Rubberband':
                methodParameters = {'num_iters': self.br_widget.rubberband_iters_spinbox.value(),
                                    'num_ranges': self.br_widget.rubberband_ranges_spinbox.value()}

            if method == 'CCAM':
                methodParameters = {'scale1': self.br_widget.ccam_scale1_spinbox.value(),
                                    'scale2': self.br_widget.ccam_scale2_spinbox.value()}

                int_flag = self.br_widget.ccam_interp_combobox.currentText()
                if int_flag == 'Linear':
                    methodParameters['int_flag'] = 0
                elif int_flag == 'Quadratic':
                    methodParameters['int_flag'] = 1
                elif int_flag == 'Spline':
                    methodParameters['int_flag'] = 2
        except:
            pass

        datakey_new = self.datakeys + '-Baseline Removed-' + method + str(methodParameters)
        datakey_baseline = datakey + '-Baseline-' + method + str(methodParameters)
        self.datakeys.append(datakey_new)
        self.datakeys.append(datakey_baseline)
        self.data[datakey_new].remove_baseline(method, segment=True, params=methodParameters)
        self.data[datakey_baseline] = spectral_data(self.data[datakey_new].df_baseline)
