import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtMultimedia import QSound
from ui_login import Ui_Form

from hans2voice import hans_voice


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.login_pushButton.clicked.connect(self.display)  # 将 clicked 事件发送出去
        self.quit_pushButton.clicked.connect(self.close)
        self.password_lineEdit.returnPressed.connect(self.display)
        self.comboBox.currentTextChanged.connect(self.choose_lang)
        self.openfile_pushButton.clicked.connect(self.readfile)
        self.chuang3bed_pushButton.clicked.connect(self.speak)
        self.chuang3bed_pushButton.clicked.connect(self.ch_hans)


    def display(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()

        if username == 'edc' and password == '123456':
            self.user_textBrowser.setText(f'Welcome, {username}!')
        else:
            self.user_textBrowser.setText('You should try it again.')

    def choose_lang(self):
        lang = self.comboBox.currentText()
        self.user_textBrowser.setText(lang)

    def readfile(self):
        file_path, ok = QFileDialog.getOpenFileName(self,
                                                    'Choose Single File',
                                                    '/Users/maccair/',
                                                    'All Files (*);;Text Files (*.txt)')
        self.user_textBrowser.setText(file_path)

    def speak(self):
        # 获得发送者，根据发送者的文本获得汉字，再从字典中找到汉字的发音。
        sender = self.sender()
        hans = sender.text()
        if hans in hans_voice:
            print('Yes, it is in.')
            self.sound = QSound(f'{hans_voice.get(hans)}.wav', self)
            self.sound.play()

    def ch_hans(self):
        self.chuang3bed_pushButton.setText('换')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyMainForm()
    my_window.show()
    sys.exit(app.exec())
