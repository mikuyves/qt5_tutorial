import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_login import Ui_Form


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyMainForm()
    my_window.show()
    sys.exit(app.exec())
