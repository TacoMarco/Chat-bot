from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from os import startfile

foods = ['nothing', 'none', 'asparagus', 'apples', 'avacado', 'alfalfa', 'acorn squash', 'almond', 'arugala', 
'artichoke', 'applesauce', 'asian noodles', 'antelope', 'ahi tuna', 'albacore tuna', 
'Apple juice', 'Avocado roll', 'Bruscetta', 'bacon', 'black beans', 'bagels', 
'baked beans', 'BBQ', 'bison', 'barley', 'beer', 'bisque', 'bluefish', 'bread', 
'broccoli', 'buritto', 'babaganoosh', 'Cabbage', 'cake', 'carrots', 'carne asada', 
'celery', 'cheese', 'chicken', 'catfish', 'chips', 'chocolate', 'chowder', 'clams', 'coffee', 
'cookies', 'corn', 'cupcakes', 'crab', 'curry', 'cereal', 'chimichanga',   'dates',
'dips', 'duck', 'dumplings', 'donuts', 'eggs', 'enchilada', 'eggrolls', 
'English muffins', 'edimame', 'eel sushi',   'fajita', 'falafel', 'fish', 'franks', 
'fondu', 'French toast', 'French dip',   'Garlic', 'ginger', 'gnocchi', 'goose', 
'granola', 'grapes', 'green beans', 'Guancamole', 'gumbo', 'grits', 'Graham crackers', 
'ham', 'halibut', 'hamburger', 'honey', 'huenos rancheros', 'hash browns', 'hot dogs', 
'haiku roll', 'hummus',   'ice cream', 'Irish stew', 'Indian food', 'Italian bread',
'jambalaya', 'jelly', 'jam', 'jerky', 'jalapeño',   'kale', 'kabobs', 
'ketchup', 'kiwi', 'kidney beans', 'kingfish',   'lobster', 'Lamb', 'Linguine', 
'Lasagna',   'Meatballs', 'Moose', 'Milk', 'Milkshake',   'Noodles',  
'Ostrich',   'Pizza', 'Pepperoni', 'Porter', 'Pancakes',   'Quesadilla', 
'Quiche',   'Reuben',  'Spinach', 'Spaghetti',   'Tater tots', 'Toast',
'Venison',  'Waffles', 'Wine', 'Walnuts',  'Yogurt',  'Ziti', 'Zucchini']

drinks = ['none','nothing', 'coke', 'Wine', 'Iced tea', 'Juice', 'Milk', 
'Beer', 'Soda', 'Coffee', 'Tea bag', 'Tea', 'Green tea', 'Chocolate milk', 
'Hot chocolate', 'Tomato juice', 'Smoothie', 'Milkshake', 'Coconut milk', 
'Orange juice', 'Lemonade', 'Fruit juice', 'Cocoa', 'Water']

class Ui_MainWindow(object):
    def g(self):
        try:
            startfile('menulist.pyw')
        except:
            pass
    # WINDOW STUFF
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 386)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 220, 361, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 321, 121))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.g())
        
        # here is break from gui
        self.lineEdit.returnPressed.connect(self.do_chatbot)

        self.state = 0
        self.fFood = None
        self.fDrink = None

        # more gui
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def find(self, lst, find):
        for i in lst:
            if find.lower() == i.lower():
                return True
        return False

    def do_chatbot(self):
        _food = self.lineEdit.text().split(' ')
        self.lineEdit.setText('')
        if self.state == 0:
            for i in _food:
                if self.find(foods,i):
                    print('food found: ' + i)
                    self.fFood = i

                if self.find(drinks,i):
                    print('drink found: ' + i)
                    self.fDrink = i

            if self.fFood == None:
                self.label.setText('What food would you like?')
                self.state = 1
                return
            
            if self.fDrink == None:
                self.label.setText('What Drink would you like with that?')
                self.state = 2
                return
            
            self.state = 3
            if self.fDrink == 'nothing' or self.fDrink == 'none':
                self.label.setText(f'Great your {self.fFood} is being delivered')
            else:
                self.label.setText(f'Great your {self.fFood} with {self.fDrink} is being delivered')

        elif self.state == 1:
            for i in _food:
                if self.find(foods,i):
                    self.fFood = i

            if self.fFood != None:
                if self.fDrink == None:
                    self.state = 2
                    self.label.setText('What Drink would you like with that?')
                else:
                    self.state = 3
                    if self.fFood == 'none' or self.fFood == 'nothing':
                        self.label.setText(f'Great your {self.fDrink} is being delivered')
                    else:
                        self.label.setText(f'Great your {self.fFood} with {self.fDrink} is being delivered')
            else:
                self.label.setText('Thats not a valid food')
        
        elif self.state == 2:
            for i in _food:
                if self.find(drinks,i):
                    self.fDrink = i
            
            if self.fDrink != None:
                self.state = 3
                self.label.setText(f'Great your {self.fFood} with {self.fDrink} is being delivered')
            else:
                self.label.setText('Thats not a valid drink')

        elif self.state == 3:
            self.label.setText('What food or drink would you like?')
            self.state = 0


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chatbot"))
        self.label.setText(_translate("MainWindow", "What food or drink would you like?"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
