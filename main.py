import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from batterywidget import BatteryWidget  # Import your BatteryWidget class

class HauptFenster(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Battery Widget Demo")

        # Create the central widget for the main window
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set a layout for the main window
        layout = QVBoxLayout(self.central_widget)

        # Create the BatteryWidget and add it to the layout
        self.battery_widget = BatteryWidget(self.central_widget)
        #self.battery_widget.setValue(50)  # Set initial battery value

        layout.addWidget(self.battery_widget)

        # Optionally, start a timer for animation (if needed)
        self.timer_id = self.startTimer(100)

    # Uncomment the following method if you want to use the timer for periodic updates
    def timerEvent(self, event):
        """Increases the battery progress cyclically."""
        value = (self.battery_widget.value + 1) % 101
        self.battery_widget.setValue(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = HauptFenster()
    fenster.show()
    sys.exit(app.exec())
