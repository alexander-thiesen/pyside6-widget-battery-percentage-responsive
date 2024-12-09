from PySide6 import QtWidgets
from batterywidget import BatteryWidget  # Import your custom BatteryWidget class

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Create the main window
    main_window = QtWidgets.QMainWindow()
    main_window.setWindowTitle("Battery Widget Demo")

    # Create an instance of BatteryWidget and set a sample battery value
    battery_widget = BatteryWidget(main_window)
    battery_widget.setValue(100)  # Example value for the battery level

    # Set the BatteryWidget as the central widget of the main window
    main_window.setCentralWidget(battery_widget)
    main_window.show()  # Display the main window

    # Start the application event loop
    sys.exit(app.exec())
