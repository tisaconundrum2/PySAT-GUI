from PyQt5 import QtGui, QtCore, QtWidgets

from Qtickle import Qtickle


class read_ccam_:
    def __init__(self, pysat_fun, module_layout, arg_list, kw_list, restr_list):
        self.qtickle = Qtickle.Qtickle(self)
        self.pysat_fun = pysat_fun
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.restr_list = restr_list
        self.module_layout = module_layout
        self.ui_id = None
        self.main()

    def main(self):
        # TODO add function param call here
        self.ui_id = self.pysat_fun.set_list(None, None, None, None, None, self.ui_id)
        self.read_ccam_ui()
        self.set_read_ccam_params()
        self.get_read_ccam_params()
        self.connectWidgets()
        self.pysat_fun.set_greyed_modules(self.read_ccam)

        # TODO add try and except here

    #        try:
    #            # arg_list.append(['known data', 5, 2, ('meta', 'SiO2')])
    #            self.create_folds.clicked.connect(
    #                lambda: self.pysat_fun.arg_list.append(['known_data', 5, 2, ('meta', 'SiO2')]))
    #        except:
    #            print('There was a problem with creating stratified folds...')

    def get_read_ccam_params(self):
        searchstring = self.read_ccam_searchstring.text()
        to_csv = self.read_ccam_outfile.text()
        searchdir = self.search_path_line_edit.text()
        try:
            lookupfile = self.metadata_file
        except:
            lookupfile = None
        args = [searchdir, searchstring]

        average = self.ave_button.isChecked()

        kws = {'to_csv': to_csv, 'lookupfile': lookupfile, 'ave': average}
        ui_list = "do_read_ccam"
        fun_list = "do_read_ccam"
        r = self.qtickle.guisave()
        self.ui_id = self.pysat_fun.set_list(ui_list, fun_list, args, kws, r, self.ui_id)

    def set_read_ccam_params(self):
        if self.restr_list is not None:
            self.qtickle.guirestore(self.restr_list)
        if self.arg_list is not None:
            searchdir = self.arg_list[0]
            searchstring = self.arg_list[1]
            to_csv = self.kw_list['to_csv']
            self.metadata_file = self.kw_list['lookupfile']
            average = self.kw_list['ave']

            self.search_path_line_edit.setText(searchdir)
            self.read_ccam_searchstring.setText(searchstring)
            self.read_ccam_outfile.setText(to_csv)
            self.metadata_line_edit.setText(str(self.metadata_file))
            if average == True:
                self.ave_button.setChecked(True)
            else:
                self.ave_button.setChecked(False)
            self.get_read_ccam_params()

    def read_ccam_ui(self):
        self.read_ccam = QtWidgets.QGroupBox()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.read_ccam.setFont(font)
        self.read_ccam.setObjectName(("Read ChemCam Data"))
        self.read_ccam_vlayout = QtWidgets.QVBoxLayout(self.read_ccam)
        self.read_ccam_vlayout.setObjectName(("read_ccam_vlayout"))

        # label and linedit for specifying search string
        self.searchstring_hlayout = QtWidgets.QHBoxLayout()
        self.read_ccam_searchstring_label = QtWidgets.QLabel(self.read_ccam)
        self.read_ccam_searchstring_label.setText('Search String: ')
        self.read_ccam_searchstring_label.setObjectName("read_ccam_searchstring_label")
        self.searchstring_hlayout.addWidget(self.read_ccam_searchstring_label)
        defaultstring = '*ccs*.csv'
        self.read_ccam_searchstring = QtWidgets.QLineEdit(self.read_ccam)
        self.read_ccam_searchstring.setText(defaultstring)
        self.read_ccam_searchstring.setObjectName("read_ccam_searchstring")
        self.searchstring_hlayout.addWidget(self.read_ccam_searchstring)
        self.read_ccam_vlayout.addLayout(self.searchstring_hlayout)

        # label and linedit for specifying search path
        self.searchpath_hLayout = QtWidgets.QHBoxLayout()
        self.search_path_label = QtWidgets.QLabel(self.read_ccam)
        self.search_path_label.setText('Search directory:')
        self.search_path_label.setObjectName("search_path_label")
        self.searchpath_hLayout.addWidget(self.search_path_label)
        self.search_path_line_edit = QtWidgets.QLineEdit(self.read_ccam)
        self.search_path_line_edit.setReadOnly(True)  # User can't edit this line
        self.search_path_line_edit.setObjectName("search_path_line_edit")
        self.searchpath_hLayout.addWidget(self.search_path_line_edit)
        self.search_path_button = QtWidgets.QToolButton(self.read_ccam)
        self.search_path_button.setText('...')
        self.search_path_button.setObjectName("search_path_button")
        self.searchpath_hLayout.addWidget(self.search_path_button)
        self.read_ccam_vlayout.addLayout(self.searchpath_hLayout)

        # label and linedit for specifying metadata
        self.metadata_hLayout = QtWidgets.QHBoxLayout()
        self.metadata_label = QtWidgets.QLabel(self.read_ccam)
        self.metadata_label.setText('Metadata file(s):')
        self.metadata_label.setObjectName("metadata_label")
        self.metadata_hLayout.addWidget(self.metadata_label)
        self.metadata_line_edit = QtWidgets.QLineEdit(self.read_ccam)
        self.metadata_line_edit.setReadOnly(True)  # User can't edit this line
        self.metadata_line_edit.setObjectName("metadata_line_edit")
        self.metadata_hLayout.addWidget(self.metadata_line_edit)
        self.metadata_button = QtWidgets.QToolButton(self.read_ccam)
        self.metadata_button.setText('...')
        self.metadata_button.setObjectName("metadata_button")
        self.metadata_hLayout.addWidget(self.metadata_button)
        self.read_ccam_vlayout.addLayout(self.metadata_hLayout)

        # label and linedit for output file
        self.outfile_hlayout = QtWidgets.QHBoxLayout()
        self.read_ccam_outfile_label = QtWidgets.QLabel(self.read_ccam)
        self.read_ccam_outfile_label.setText('Output file name:')
        self.read_ccam_outfile_label.setObjectName("read_ccam_outfile_label")
        self.outfile_hlayout.addWidget(self.read_ccam_outfile_label)

        self.read_ccam_outfile = QtWidgets.QLineEdit(self.read_ccam)
        self.read_ccam_outfile.setObjectName("read_ccam_outfile")
        self.outfile_hlayout.addWidget(self.read_ccam_outfile)
        self.read_ccam_vlayout.addLayout(self.outfile_hlayout)

        # ave vs singleshot buttons
        self.ave_hlayout = QtWidgets.QHBoxLayout()
        self.ave_button = QtWidgets.QRadioButton('Averages')
        self.singleshot_button = QtWidgets.QRadioButton('Single Shots')
        self.ave_button.setObjectName("ave_button")
        self.ave_hlayout.addWidget(self.ave_button)
        self.singleshot_button.setObjectName("singleshot_button")
        self.ave_hlayout.addWidget(self.singleshot_button)
        self.ave_button.setChecked(True)
        self.read_ccam_vlayout.addLayout(self.ave_hlayout)

        self.read_ccam.setTitle("Read ChemCam Data")
        self.read_ccam.setObjectName("read_ccam")
        self.module_layout.addWidget(self.read_ccam)

    def connectWidgets(self):
        self.read_ccam_searchstring.textChanged.connect(lambda: self.get_read_ccam_params())
        self.read_ccam_outfile.textChanged.connect(lambda: self.get_read_ccam_params())
        self.search_path_button.clicked.connect(lambda: self.on_searchpathButton_clicked())
        self.metadata_button.clicked.connect(lambda: self.on_metadataButton_clicked())
        self.ave_button.toggled.connect(lambda: self.get_read_ccam_params())
        self.singleshot_button.toggled.connect(lambda: self.get_read_ccam_params())


    # def read_ccam_change_vars(self):
    #     self.read_ccam_choose_var.clear()
    #     choices = self.pysat_fun.data[self.read_ccam_choose_data.currentText()].df['meta'].columns.values
    #
    #     self.read_ccam_choose_var.addItems(choices)
    #
    # def read_ccam_change_testfolds(self):
    #     self.choose_test_fold.clear()
    #     choices = list(map(str, list(range(1, self.nfolds_spin.value() + 1))))
    #     print(choices)
    #     self.choose_test_fold.addItems(choices)

    def on_searchpathButton_clicked(self):
        dirname = QtWidgets.QFileDialog.getExistingDirectory(parent=None, caption="Select Search Directory",
                                                             directory='.')
        self.search_path_line_edit.setText(dirname)
        if self.search_path_line_edit.text() == "":
            self.search_path_line_edit.setText("*/")
        self.get_read_ccam_params()

    def on_metadataButton_clicked(self):
        self.metadata_file, null = QtWidgets.QFileDialog.getOpenFileNames(parent=None,
                                                                          caption="Select metadata file(s)",
                                                                          directory='.')
        self.metadata_line_edit.setText(str(self.metadata_file))
        if self.metadata_line_edit.text() == "":
            self.metadata_line_edit.setText("*/")
        self.get_read_ccam_params()
