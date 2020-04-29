所有 App 界面上看到的内容都是一个组件 widget。

包括：
buttons, labels, windows, dialogs, progress bars 等等。

类似 HTML 元素一样，经常一个嵌套另一个。

一个按钮 Button 上包含一个标签 Label

![img](https://build-system.fman.io/static/public/img/widgets.png)

[此图的代码](a04_widgets_example.py)
报错：
```
Traceback (most recent call last):
  File "widgets_example.py", line 44, in <module>
    from fbs_runtime.application_context.PyQt5 import ApplicationContext
ModuleNotFoundError: No module named 'fbs_runtime'
```


# 页面设计与业务逻辑分离
编写逻辑文件是 Class 的设置

如有报错为 `AttributeError: '***' object has no attribute 'setCentralWidget'`，很可能是没有继承 QMainWindow。

类 必须继承 QMainWindow 及 生成 ui_**.py 文件的 Ui_MainWindow/Ui_Form/等 两个类。

继承之后初始化调用 super 函数超类的 __init__() 方法初始化，需要两个参数：
第一个参数，自定义类，说明想要调用超类的某个方法，这里的超类，即 QMainWindow 和 UiMainWindow/Ui_Form。
第二个参数，self，引用的是刚刚实例化出来的自己，于是超类就能得到这个对象self，并向其添加 parent 特性，这里 parent=None，QMainWindow 的__init__()方法中默认值就是None，其实可以用不添加。

超类初始化后，调用 QMainWindow/Ui_Form 的 setupUi() 方法，把 self 对象传入。
否则不能引用 ui_**.py 中的所有组件。

 
```Python
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_stackwidget import Ui_MainWindow


class MyStackWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyStackWidget, self).__init__(parent)
        self.setupUi(self)
```

Python3 中，可以简写成：
```Python
class MyStackWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init()
        self.setupUi(self)
```
