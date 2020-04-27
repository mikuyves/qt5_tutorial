from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])  # 初始化一个 app 实例。
# app.setStyle('Fusion')  # 设置一种风格。
window = QWidget()  # 创建一个窗口。
layout = QVBoxLayout()  # 创建一个 layout 实例。
layout.addWidget(QPushButton('Top'))  # 创建一个按钮。
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)  # 将 layout 放在窗口中。
window.show()  # 显示窗口。
app.exec_()  # 执行 app()。