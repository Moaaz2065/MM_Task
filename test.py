import sys
import pytest
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2 import QtCore
from main import MainWindow

@pytest.fixture
def app(qtbot):
    """Fixture to initialize the application."""
    application = QApplication.instance()
    if application is None:
        application = QApplication(sys.argv)
    window = MainWindow()
    qtbot.addWidget(window)
    return window

def test_input_validation_empty_fields(app, qtbot):
    """Test input validation for empty fields."""
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    
    message_box = app.findChild(QMessageBox)
    assert message_box is not None
    assert "Error in Function 1" in message_box.windowTitle()

def test_input_validation_invalid_function1(app, qtbot):
    """Test input validation for invalid Function 1."""
    qtbot.keyClicks(app.function1_input, "x^2 + invalid")
    qtbot.keyClicks(app.function2_input, "x + 1")
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    
    message_box = app.findChild(QMessageBox)
    assert message_box is not None
    assert "Error in Function 1" in message_box.windowTitle()

def test_input_validation_invalid_function2(app, qtbot):
    """Test input validation for invalid Function 2."""
    qtbot.keyClicks(app.function1_input, "x^2 + 1")
    qtbot.keyClicks(app.function2_input, "x + invalid")
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    
    message_box = app.findChild(QMessageBox)
    assert message_box is not None
    assert "Error in Function 2" in message_box.windowTitle()

def test_plot_functions_valid_input(app, qtbot):
    """Test plotting with valid input."""
    qtbot.keyClicks(app.function1_input, "x^2")
    qtbot.keyClicks(app.function2_input, "2*x")
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    
    message_box = app.findChild(QMessageBox)
    assert message_box is None 