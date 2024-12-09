# Fork of
# Battery Widget
# Author: Theara Kong
# Email: theara729@gmail.com
# GitHub: https://github.com/Ktheara

# Responsive Battery Widget
# Author: Alexander Thiesen
# GitHub: https://github.com/alexander-thiesen

from PySide6 import QtWidgets
from PySide6.QtCore import Slot

class BatteryWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Create the main container widget
        self.wg_container = QtWidgets.QWidget(self)
        self.wg_container.setStyleSheet("""
            #wg_container {
                background: rgba(0, 0, 0, 0);  # Transparent background
            }
        """)
        self.wg_container.setObjectName("wg_container")

        # Create the battery head (small rectangle at the top)
        self.body_head = QtWidgets.QLabel(self.wg_container)
        self.body_head.setStyleSheet("""
            #body_head {
                background: #ffffff;  # White background for the head
                border-radius: 2px;  # Rounded corners
            }
        """)
        self.body_head.setText("")  # No text inside the head
        self.body_head.setObjectName("body_head")

        # Create the battery body (main rectangle area)
        self.body = QtWidgets.QLabel(self.wg_container)
        self.body.setStyleSheet("""
            #body {
                border: 3px ridge #ffffff;  # White ridged border
                border-radius: 5px;  # Rounded corners
            }
        """)
        self.body.setText("")  # No text inside the body
        self.body.setObjectName("body")

        # Create the battery level bars (5 sections for different levels)
        self.level_labels = []
        for i in range(5):
            label = QtWidgets.QLabel(self.wg_container)
            label.setStyleSheet(f"""
                #lvl_{i+1} {{
                    background: #7CFC00;  # Default green color for active levels
                }}
            """)
            label.setText("")  # No text for the level bars
            label.setObjectName(f"lvl_{i+1}")
            self.level_labels.append(label)

        # Set an initial battery value (50%)
        self.setValue(50)

    def resizeEvent(self, event):
        """
        Handle resizing of the widget and adjust the size/position
        of all components dynamically.
        """
        super().resizeEvent(event)

        # Get the current widget dimensions
        width, height = self.width(), self.height()

        # Adjust the main container to match the widget size
        container_width = width * 1
        container_height = height * 1
        self.wg_container.setGeometry(0, 0, container_width, container_height)

        # Calculate and set dimensions for the battery head
        head_width = container_width * 0.06
        head_height = container_height * 0.4
        self.body_head.setGeometry(container_width - head_width, container_height * 0.3, head_width, head_height)

        # Calculate and set dimensions for the battery body
        body_width = container_width - head_width
        body_height = container_height * 1
        self.body.setGeometry(0, 0, body_width, body_height)

        # Calculate spacing and size for the battery level bars
        level_spacing = body_width * 0.05  # Spacing between level bars
        level_width = (body_width - (6 * level_spacing)) / 5  # Width of each level bar
        level_height = body_height * 0.8  # Height of each level bar
        for i, label in enumerate(self.level_labels):
            x_pos = level_spacing + i * (level_width + level_spacing)  # Horizontal position
            label.setGeometry(x_pos, body_height * 0.1, level_width, level_height)



    @Slot(int)
    def setValue(self, value):
        """
        Set the battery charge level and update the display.
        Adjust the charge level value to ensure it is within the range 0-100.
        """
        # Clamp the value to the range 0-100
        self.value = max(0, min(100, value))

        # Set battery style based on charge level thresholds
        if self.value < 5:
            # Very low charge: Red color and no bars active
            self.setBatteryStyle("#FF0000", "#FF0000", [0, 0, 0, 0, 0])
        elif self.value <= 20:
            # Low charge: Red color with 1 bar active
            self.setBatteryStyle("#FFFFFF", "#FF0000", [1, 0, 0, 0, 0])
        elif self.value <= 40:
            # Medium-low charge: Orange color with 2 bars active
            self.setBatteryStyle("#FFFFFF", "#F28500", [1, 1, 0, 0, 0])
        elif self.value <= 60:
            # Medium charge: Yellow color with 3 bars active
            self.setBatteryStyle("#FFFFFF", "#ffd700", [1, 1, 1, 0, 0])
        elif self.value <= 80:
            # High charge: Light green color with 4 bars active
            self.setBatteryStyle("#FFFFFF", "#32cd32", [1, 1, 1, 1, 0])
        else:
            # Full charge: Bright green color with all bars active
            self.setBatteryStyle("#FFFFFF", "#7CFC00", [1, 1, 1, 1, 1])

        # Update the container display
        self.wg_container.update()

    def setBatteryStyle(self, borderColor, color, levels):
        """
        Set the battery display style based on the border color,
        active bar color, and active/inactive status of each bar.
        :param borderColor: Color of the battery frame and head
        :param color: Color of the active level bars
        :param levels: List indicating which bars are active (e.g., [1, 1, 0, 0, 0])
        """
        # Update the battery head style
        self.body_head.setStyleSheet(f"""
            #body_head {{
                background: {borderColor};
                border-radius: 2px;
            }}
        """)
        # Update the battery body style
        self.body.setStyleSheet(f"""
            #body {{
                border: 3px ridge {borderColor};
                border-radius: 5px;
            }}
        """)

        # Update the individual level bars
        for i, label in enumerate(self.level_labels):
            if levels[i]:
                # Active bars are displayed with the specified color
                label.setStyleSheet(f"#lvl_{i+1} {{ background: {color}; }}")
            else:
                # Inactive bars are made transparent
                label.setStyleSheet(f"#lvl_{i+1} {{ background: rgba(0, 0, 0, 0); }}")
