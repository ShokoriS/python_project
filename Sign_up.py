try:
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
    from PyQt5.Qt import Qt
    from PyQt5.QtGui import QIcon, QPixmap
    from PyQt5.QtCore import QTimer
    import pymysql
    from pymysql import Error
    import logging
except ModuleNotFoundError as mr:
    logging.info(mr)
logging.basicConfig(filename="log_document.txt", level=logging.INFO)


class DB_Connect_Sign_up:

    def __init__(self, host, user, password, database):
        self.connection = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect_to_db(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database)

        except Error as e:
            print(f"Connection failed ! because {e}")


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

        self.db_connect = DB_Connect_Sign_up("localhost", "Shokori", "max(1,2,3)is3", "task_manger")

        self.loading = QLabel("", self)
        self.timer = QTimer(self)
        self.dot = ""

        # Set up the interface
        self.init_ui()

    def init_ui(self):
        self.db_connect.connect_to_db()
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

        self.loading.setStyleSheet(
            "color:white;"
            "font-family:Arial;"
            "font-size:20px;"
            "margin:50px;")

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
        vbox.addWidget(self.loading, alignment=Qt.AlignCenter)
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

    def submit(self):
        cursor = self.db_connect.connection.cursor()
        user = self.user_name_email.text().strip()
        password = self.user_password.text().strip()

        if not user or not password:  # Check if fields are empty
            self.user_name_email.setPlaceholderText("Please fill out this form > Username")
            self.user_password.setPlaceholderText("Please fill out this form > Password")
            return

        if user == password:
            self.user_name_email.clear()
            self.user_password.clear()
            self.user_name_email.setPlaceholderText("Username and password can't be the same!")
            return

        if len(password) < 4:
            self.user_password.clear()
            self.user_password.setPlaceholderText("Please enter more than 4 characters")
            return

        # Check if username already exists
        identical_user = "SELECT username_email FROM user WHERE username_email = %s;"
        cursor.execute(identical_user, (user,))
        result = cursor.fetchone()

        if result or user.isdigit():
            self.user_name_email.clear()
            self.user_name_email.setPlaceholderText("Please enter another username!")
            return



        # Insert the user into the database
        sql_command = "INSERT INTO user(username_email, password) VALUES (%s, %s);"
        cursor.execute(sql_command, (user, password))
        self.db_connect.connection.commit()

        # Start the timer for loading animation
        self.timer.timeout.connect(self.update)
        self.timer.start(700)

    # I can use the timer to update the (.) dot
    def update(self):
        self.dot += "."
        self.loading.setText(f"Loading{self.dot}")
        if len(self.dot) >= 6:
            self.timer.stop()
            self.loading.setText("Done!")


def main():
    app = QApplication(sys.argv)
    window = SignUPWindow()
    window.show()
    sys.exit(app.exec_())


try:
    main()

except ModuleNotFoundError as em:
    logging.info(em)

except Exception as e:
    logging.info(e)

except Error as er:
    logging.info(er)

