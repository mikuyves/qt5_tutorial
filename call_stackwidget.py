import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from hanziconv import HanziConv

from ui_stackwidget import Ui_MainWindow
from poems import poems


class MyStackWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.currentTextChanged.connect(self.get_poem)
        self.chs_checkBox.stateChanged.connect(self.cht2chs)
        self.get_poem()

    def get_poem(self):
        title = self.comboBox.currentText()
        for k, v in poems.items():
            if k == title:
                self.title_label.setText(v.get('title'))
                self.author_label.setText(v.get('author'))
                type_id = v.get('type_id')
                for index, char in enumerate(v.get('content'), start=1):
                    i_str = str(index).zfill(2)  # 数字补全 0 位，使用 sting.zfill(<位>)
                    button = self.findChild(QPushButton, f'{type_id}_{i_str}_pushButton')
                    button.setText(char)

    def cht2chs(self):
        if self.chs_checkBox.isChecked():
            buttons = self.findChildren(QPushButton)
            labels = self.findChildren(QLabel)
            for btn in buttons:
                btn.setText(HanziConv.toSimplified(btn.text()))
            for lb in labels:
                lb.setText(HanziConv.toSimplified(lb.text()))
        else:
            self.get_poem()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyStackWidget()
    my_window.show()
    sys.exit(app.exec())
