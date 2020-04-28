import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_login import Ui_Form


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.login_pushButton.clicked.connect(self.display)  # 将 clicked 事件发送出去
        self.quit_pushButton.clicked.connect(self.close)
        self.password_lineEdit.returnPressed.connect(self.display)

    def display(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()

        if username == 'edc' and password == '123456':
            self.user_textBrowser.setText(f'Welcome, {username}!')
        else:
            self.user_textBrowser.setText('You should try it again.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyMainForm()
    my_window.show()
    sys.exit(app.exec())
