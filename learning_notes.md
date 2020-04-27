所有 App 界面上看到的内容都是一个组件 widget。

包括：
buttons, labels, windows, dialogs, progress bars 等等。

类似 HTML 元素一样，经常一个嵌套另一个。

一个按钮 Button 上包含一个标签 Label

![img](https://build-system.fman.io/static/public/img/widgets.png)

[此图的代码](a04_widgets_example.py)
报错：
``````
Traceback (most recent call last):
  File "widgets_example.py", line 44, in <module>
    from fbs_runtime.application_context.PyQt5 import ApplicationContext
ModuleNotFoundError: No module named 'fbs_runtime'
```