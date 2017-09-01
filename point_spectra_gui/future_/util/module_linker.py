class Module:
    nodeCount = 0

    def __init__(self, ui_list, fun_list, arg_list, kw_list, ui_restore):
        self.ui_list = ui_list
        self.fun_list = fun_list
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_restore = ui_restore
        self.next = None
        self.UI_ID = Module.nodeCount
        Module.nodeCount += 1

    def setData(self, ui_list, fun_list, arg_list, kw_list, ui_restore):
        self.ui_list = ui_list
        self.fun_list = fun_list
        self.arg_list = arg_list
        self.kw_list = kw_list
        self.ui_restore = ui_restore

    def getID(self):
        return self.UI_ID

    def getData(self):
        list = []
        list.append(self.getID())
        list.append(self.ui_list)
        list.append(self.fun_list)
        list.append(self.arg_list)
        list.append(self.kw_list)
        list.append(self.ui_restore)
        return list

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next