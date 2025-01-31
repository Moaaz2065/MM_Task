import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PySide2.QtGui import QFont
import validation
import plotting

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPointSize(18)

        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 400, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.function1_input = QLineEdit(self)
        self.function1_input.setPlaceholderText("Enter Function")
        self.function1_input.setFixedHeight(50)
        self.function1_input.setFixedWidth(200)
        self.function1_input.setFont(QFont().setPointSize(18))
        h_layout.addWidget(self.function1_input)
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(h_layout)

        h_layout = QHBoxLayout()
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.function2_input = QLineEdit(self)
        self.function2_input.setPlaceholderText("Enter Function")
        self.function2_input.setFixedHeight(50)
        self.function2_input.setFixedWidth(200)
        self.function2_input.setFont(QFont().setPointSize(18))
        h_layout.addWidget(self.function2_input)
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(h_layout)

        h_layout = QHBoxLayout()
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.plot_button = QPushButton("Plot Functions", self)
        self.plot_button.setFixedWidth(200)
        self.plot_button.setFixedHeight(50)
        h_layout.addWidget(self.plot_button)
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(h_layout)

        central_widget.setLayout(layout)

        self.plot_button.clicked.connect(self.on_plot_button_clicked)

    def on_plot_button_clicked(self):
        """Handle the button click event."""
        function1 = self.function1_input.text()
        function2 = self.function2_input.text()
        valid1, exp1 = validation.validateEquation(function1)
        valid2, exp2 = validation.validateEquation(function2)
        print(exp1, exp2)
        if not valid1 :
            QMessageBox.critical(self, "Error in Function 1", f'{exp1}')
            return
        if not valid2 : 
            QMessageBox.critical(self, "Error in Function 2", f'{exp2}')
            return
        plotting.plot_functions(function1, function2)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())