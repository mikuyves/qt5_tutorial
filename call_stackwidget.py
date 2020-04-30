import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from hanziconv import HanziConv
from PyQt5.QtCore import QObject, pyqtSignal

from ui_stackwidget import Ui_MainWindow
from poems import poems, page_id


class Communicate(QObject):
    click_button = pyqtSignal()


class MyStackWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.currentTextChanged.connect(self.get_poem)
        self.chs_checkBox.stateChanged.connect(self.cht2chs)

        self.get_poem()

        # 多个按钮绑定一个 slot，常规需要每个按钮写一个 pushButton.clicked.connect(<slot>)
        # 用 findChildren 找出所有按钮，然后 for 筛选之后绑定同一个 slot。
        # slot 函数中，用 sender 找出这个 signal 是来自哪个 sender。
        buttons = self.findChildren(QPushButton)
        for btn in buttons:
            if btn.objectName()[:2] in page_id:
                btn.clicked.connect(self.button_click)

    def button_click(self):
        sender = self.sender()
        btn_text = sender.text()
        print(btn_text)

    def get_poem(self):
        title = self.comboBox.currentText()
        if title in poems:
            p = poems.get(title)
            p_title = p.get('title')
            p_author = p.get('author')
            p_content = p.get('content')
            p_type_id = p.get('type_id')

            self.title_label.setText(p_title)
            self.author_label.setText(p_author)

            if p_type_id == 'j5':
                self.stackedWidget.setCurrentIndex(0)
            if p_type_id == 'j7':
                self.stackedWidget.setCurrentIndex(1)

            for i, char in enumerate(p_content, start=1):
                i_str = str(i).zfill(2)  # 数字补全 0 位，使用 sting.zfill(<位>)
                button = self.findChild(QPushButton, f'{p_type_id}_{i_str}_pushButton')
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
