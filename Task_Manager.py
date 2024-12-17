import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.Qt import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setStyleSheet("background-color:#1f2121;")
        self.setGeometry(0, 0, 1920, 1080)

        self.central_widget.setStyleSheet("background-color: gray;")
        self.icon = QPixmap("f53601133f236d1cb167ac19f05a3d60.gif")
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle("Task Manager")

        # Load and scale the main photo
        self.main_photo = QPixmap("f53601133f236d1cb167ac19f05a3d60.gif")
        self.main_photo = self.main_photo.scaled(1620, 500, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.main_photo_label = QLabel(self)
        self.main_photo_label.setPixmap(self.main_photo)
        self.main_photo_label.setFixedSize(1550, 500)
        self.main_photo_label.setAlignment(Qt.AlignCenter)

        # Buttons and other widgets
        self.add_new_task = QPushButton("Add new tasks", self)
        self.add_task = QPushButton("Add to existing tasks", self)
        self.write_to_tasks = QPushButton("Write to tasks", self)

        self.vertical_line = QFrame(self)
        self.coming_soon = QLabel("More functionalities will \nbe added...", self)

        self.show_username = QLabel("Welcome back \n <username>", self)

        self.init_ui()

    def init_ui(self):
        # Button sizes
        self.add_task.setFixedSize(300, 50)
        self.add_new_task.setFixedSize(300, 50)
        self.write_to_tasks.setFixedSize(300, 50)

        # Stylesheet for buttons
        self.central_widget.setStyleSheet("""
            QPushButton {
                font-size:20px;
                font-family:Arial;
                background-color:#303333;
                color:white;
                border:0.1px solid gray;
                border-radius:5px;
                padding:10px;
            }

            QPushButton:hover {
                background-color:gray;
                border:2px solid #303333;
            }
            QPushButton:pressed {
                background-color:#91918e;
            }
            """)

        # Additional styles
        self.main_photo_label.setStyleSheet("background-color:black;")
        self.coming_soon.setFixedSize(300, 200)
        self.coming_soon.setStyleSheet("""font-size:20px;
                font-family:Arial;
                color:white;
                margin:12px;""")

        self.show_username.setStyleSheet("""font-size:45px;
                font-family:Arial;
                color:white;
                margin:10 0 50 0px;""")

        # Create the vertical line using QFrame
        self.vertical_line.setFrameShape(QFrame.VLine)  # Vertical line
        self.vertical_line.setFrameShadow(QFrame.Sunken)  # Optional for a 3D effect
        self.vertical_line.setStyleSheet("background-color:#91918e;")  # White color
        self.vertical_line.setFixedWidth(1)  # Set the line thickness

        # Create layouts
        left_layout = QVBoxLayout()  # Buttons on the left
        left_layout.addWidget(self.show_username, alignment=Qt.AlignLeft)
        left_layout.addWidget(self.add_new_task, alignment=Qt.AlignLeft)
        left_layout.addWidget(self.add_task, alignment=Qt.AlignLeft)
        left_layout.addWidget(self.write_to_tasks, alignment=Qt.AlignLeft)
        left_layout.addWidget(self.coming_soon, alignment=Qt.AlignLeft)
        left_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        main_layout = QHBoxLayout()  # Combine the left layout and the line
        main_layout.addLayout(left_layout)  # Add buttons layout
        main_layout.addWidget(self.vertical_line, alignment=Qt.AlignLeft)  # Add the vertical line
        main_layout.addWidget(self.main_photo_label, alignment=Qt.AlignCenter | Qt.AlignTop)
        main_layout.setAlignment(Qt.AlignLeft)

        self.central_widget.setLayout(main_layout)  # Set main layout to the central widget


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
