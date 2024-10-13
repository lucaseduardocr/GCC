from PyQt5.QtWidgets import *

app = QApplication([])
label = QLabel('Hello Word')
label.setGeometry(100,100,100,100)

label.show()
app.exec_()
