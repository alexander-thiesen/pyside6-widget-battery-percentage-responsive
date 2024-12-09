# PySide6 Battery Percentage Widget (Responsive Version)

I updated the widget of https://github.com/Ktheara/pyqt5-widget-battery-percentage to be responsive to size changes. Additionally, I switched from PyQt5 to PySide6, as it offers better support and more modern features. 

![Imgae](https://github.com/Ktheara/pyqt5-widget-battery-percentage/blob/main/image/pyqt5-battery-widget.png)

## Setup

1. If you're using Qt Designer, promot your widget to `BatteryWidget`
2. Copy `batterywidget.py` to your main directory
3. To set the battery value use:
    ```python
    self.yourUIbatteryWidgetName.setValue(value) # between 0 - 100, percentage
    ```

# Note
- This widget is responsive, meaning it will adjust to different screen sizes.
It now uses PySide6 instead of PyQt5.
The widget is resizable and the behavior can be further customized in `batterywidget.py`.
- This is a fork of https://github.com/Ktheara/pyqt5-widget-battery-percentage
