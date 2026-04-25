import sys # For system-specific parameters and functions, like exiting the app
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QListWidget, QMessageBox) # For creating the GUI components and layouts run the installer: "pip install PyQt6"
from PyQt6.QtCore import Qt # For alignment and other core features

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the User Interface
        self.init_ui()

    def init_ui(self):
        # 1. Window Settings
        self.setWindowTitle("ProTask Manager")
        self.setGeometry(100, 100, 400, 500)

        # 2. Widgets
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.task_input.returnPressed.connect(self.add_task) # Add on Enter key

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        self.task_list = QListWidget()

        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.setObjectName("deleteBtn") # For specific styling
        self.delete_button.clicked.connect(self.delete_task)

        # 3. Layouts
        # Input row (Horizontal)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        # Main Layout (Vertical)
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addWidget(self.delete_button)

        self.setLayout(main_layout)

        # 4. Apply Intermediate Styling (QSS)
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
                font-family: Arial;
                font-size: 14px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #34495e;
                border-radius: 4px;
                background-color: #34495e;
            }
            QPushButton {
                background-color: #27ae60;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
            QPushButton#deleteBtn {
                background-color: #c0392b;
            }
            QPushButton#deleteBtn:hover {
                background-color: #e74c3c;
            }
            QListWidget {
                background-color: #34495e;
                border-radius: 4px;
                padding: 5px;
            }
        """)

    # --- Logic / Slots ---

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Empty Task", "Please enter some text!")

    def delete_task(self):
        selected_item = self.task_list.currentRow()
        if selected_item >= 0:
            self.task_list.takeItem(selected_item)
        else:
            QMessageBox.information(self, "Selection", "Select a task to delete first.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec())