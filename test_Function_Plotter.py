import pytest
import sys
from PySide2.QtWidgets import QApplication, QMessageBox, QWidget
from PySide2.QtCore import Qt
from Function_Plotter import MainWindow


@pytest.fixture(scope="session")
def app(request):
    """Create a QApplication instance for the test session."""
    
    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    request.addfinalizer(app.quit)
    
    return app


@pytest.fixture
def mainWindow(app, qtbot):
    """Create a MainWindow instance for each test and add it to the QApplication."""
    
    window = MainWindow()
    qtbot.addWidget(window)
    
    return window


def test_plot_valid_function(mainWindow, qtbot):
    # Set valid inputs
    mainWindow.txtEquation.setText("x^2")
    mainWindow.txtMinimumX.setText("-10")
    mainWindow.txtMaximumX.setText("10")

    # Simulate button click
    qtbot.mouseClick(mainWindow.btnPlot, Qt.LeftButton)

    # Check if the plot is displayed
    assert mainWindow.figure.axes


if __name__ == "__main__":
    pytest.main()
