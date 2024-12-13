import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon, QPixmap


class SignUPWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Task Manager")

        # Set up the Icon for the window
        icon = QPixmap("f53601133f236d1cb167ac19f05a3d60.gif")
        self.setWindowIcon(QIcon(icon))

        # Create the central widget and set its size
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Set up the central widget color
        self.central_widget.setStyleSheet("background-color: #1f2121;")

        # Create widgets
        self.signup = QLabel("Sign up", self)
        self.user_name_email = QLineEdit(self)
        self.user_password = QLineEdit(self)

        # Submit button
        self.submit_button = QPushButton("Submit", self)

        # Toggle button for password visibility
        self.toggle_button = QPushButton("🙈", self)
        self.password_visible = False

        # Set up the interface
        self.init_ui()

    def init_ui(self):
        # Configure the username, email line edit
        self.user_name_email.setPlaceholderText("Username or Email address")
        self.user_name_email.setFixedSize(400, 50)
        self.user_name_email.setStyleSheet(
            "font-size:20px;"
            "font-family:Arial;"
            "color:white;"
            "border:2px solid gray;"
            "border-radius:13px;"
        )

        # Configure the user password line edit
        self.user_password.setPlaceholderText("Password")
        self.user_password.setFixedSize(375, 50)
        self.user_password.setEchoMode(QLineEdit.Password)  # Hide password input initially
        self.user_password.setStyleSheet(
            "font-size:20px;"
            "font-family:Arial;"
            "color:white;"
            "border:2px solid gray;"
            "border-radius:13px;"
        )

        # Connect toggle button to slot
        self.toggle_button.clicked.connect(self.toggle_clicked)

        # Configure the label
        self.signup.setStyleSheet(
            "color:white;"
            "font-family:Arial;"
            "font-size:30px;"
            "margin:20px;"
        )

        self.submit_button.clicked.connect(self.submit)
        
        # Configure the submit button
        self.submit_button.setFixedSize(200, 50)
        self.submit_button.setStyleSheet(
            """
            QPushButton {
                font-size:18px;
                font-family:Arial;
                color:white;
                border:2px solid gray;
                border-radius:10px;
                padding:10px;
            }
            QPushButton:hover {
                background-color:#303333;
                border:2px solid #303333;
            }
            QPushButton:pressed {
                background-color:gray;
            }
            """
        )

        # Configure the toggle button
        self.toggle_button.setStyleSheet(
            """
            QPushButton {
                background-color:#1f2121;
                border:None;
            }
            QPushButton:pressed {
                background-color:gray;
            }
            """
        )

        # Create a horizontal layout for the password field and the toggle button
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.user_password, alignment=Qt.AlignCenter)
        password_layout.addWidget(self.toggle_button, alignment=Qt.AlignRight)
        password_layout.setAlignment(Qt.AlignCenter)  # Center the layout

        # Add the horizontal layout for the password field into the main layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.signup, alignment=Qt.AlignCenter)  # Center the label
        vbox.addWidget(self.user_name_email, alignment=Qt.AlignCenter)  # Center username/email input
        vbox.addLayout(password_layout)  # Add the password and toggle button layout
        vbox.addWidget(self.submit_button, alignment=Qt.AlignCenter)  # Center submit button
        vbox.setAlignment(Qt.AlignCenter)  # Center the entire layout

        # Set the layout for the central widget
        self.central_widget.setLayout(vbox)

    def toggle_clicked(self):
        if self.password_visible:
            self.user_password.setEchoMode(QLineEdit.Password)  # Hide password
            self.toggle_button.setText("🙈")  # Update button icon
        else:
            self.user_password.setEchoMode(QLineEdit.Normal)  # Show password
            self.toggle_button.setText("🙊")  # Update button icon
        self.password_visible = not self.password_visible  # Toggle the flag

    
        self.submit()

    def submit(self):
        user = self.user_name_email.text()
        password = self.user_password.text()

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignUPWindow()
    window.show()
    sys.exit(app.exec_())


