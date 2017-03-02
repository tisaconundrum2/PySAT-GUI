# class List:
#     def __init__(self):
#         self.head = None
#
#     def push(self, data, UI_ID):
#         if not self.amend(data, UI_ID):  # if we can't find a similar UI_ID then we'll go ahead and add the new data
#             temp = Node(data, UI_ID)
#             temp.setNext(self.head)
#             self.head = temp
#
#     def amend(self, data, UI_ID):
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.getID() == UI_ID:
#                 found = True
#                 current.setData(data)
#             else:
#                 current = current.getNext()
#         return found
#
#     def pop(self):
#         current = self.head
#         previous = None
#         while current.getNext() != None:
#             previous = current
#             current = current.getNext()
#         if previous == None:
#             self.head = current.getNext()
#         else:
#             previous.setNext(current.getNext())
#             return current.getData()
#
#     def size(self):  # We'll want the size so that we don't go over limit when working with for loops
#         current = self.head
#         count = 0
#         while current is not None:
#             count += 1
#             current = current.getNext()
#         return count
#
#     def remove(self, func_name):
#         """
#         Remove will allow us to remove entire pieces of a module out.
#         this will be handy in the delete layout modules
#         :param func_name:
#         :return:
#         """
#         current = self.head
#         previous = None
#         found = False
#         while not found:
#             if current.getFunList() == func_name:
#                 found = True
#             else:
#                 previous = current
#                 current = current.getNext()
#
#         if previous == None:
#             self.head = current.getNext()
#         else:
#             previous.setNext(current.getNext())
#
#     def display(self):
#         current = self.head
#         previous = None
#         while current != None:
#             print(current.getData())
#             previous = current
#             current = current.getNext()
