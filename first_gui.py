from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])  # 新建一个App，[] 命令行参数。
label = QLabel('Hello world!')  # 新建一个 Label。
label.show()  # 在荧屏上显示。
app.exec()  # 执行直至关闭。

