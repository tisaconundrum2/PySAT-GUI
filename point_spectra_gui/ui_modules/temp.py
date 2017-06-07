def restore_first(self):
    try:
        self.r_list = self.restore_list.pop()
        while self.r_list[1] == "do_get_data" or self.r_list[1] == 'do_read_ccam':
            getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
            print(self.r_list)
            self.r_list = self.restore_list.pop()
        self.on_okButton_clicked()
        self.pysat_fun.taskFinished.connect(self.restore_rest)
    except Exception as e:
        print(e)


def restore_rest(self):
    if self.restore_flag is False:
        getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
        for i in range(len(self.restore_list)):
            self.r_list = self.restore_list.pop()
            print(self.r_list)
            getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
        self.restore_flag = True





def restore(self):
    if self.restore_flag is False:
        getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
        for i in range(len(self.restore_list)):
            self.r_list = self.restore_list.pop()
            print(self.r_list)
            getattr(pysat_ui, self.r_list[1])(self, self.r_list[3], self.r_list[4])
        self.restore_flag = True
