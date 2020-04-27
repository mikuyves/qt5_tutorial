import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 800)
    w.move(300, 300)
    w.setWindowTitle('This is a Qt5 window.')
    w.show()

    sys.exit(app.exec_())
