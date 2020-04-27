from PyQt5.QtWidgets import *


app = QApplication([])
button = QPushButton('Click')

# 注意这是 C++ 中 slot 的概念，但在 python 中跟普通函数一样。
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)  # clicked 是一个信号Signal传入Slot*
button.show()
app.exec_()
