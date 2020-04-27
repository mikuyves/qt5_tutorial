from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])  # 新建一个App，[] 命令行参数。
label = QLabel('Hello world!')  # 新建一个 Label。
label.show()  # 在荧屏上显示。
app.exec_()  # 执行直至关闭。exec_()之所以有个下划线，是因为exec是一个Python的关键字。

