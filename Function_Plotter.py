import re
import sys
import numpy as np
import sympy as sp
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox,QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting the title and the icon of the app.
        self.setWindowTitle("Function Plotter")
        self.setWindowIcon(QIcon("images/icon.png"))
        self.resize(900, 600)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        # Creating the main container (widget) and setting it as the main window's central widget.
        containerWidget = QWidget()
        self.setCentralWidget(containerWidget)

        # Creating the layout for the container.
        layout = QGridLayout()
        containerWidget.setLayout(layout)

        # Creating input fields and button for plotting the function.
        self.txtEquation = QLineEdit()
        self.txtMinimumX = QLineEdit()
        self.txtMaximumX = QLineEdit()
        
        self.btnPlot = QPushButton("Plot")

        # Adding the input fields and the button to the container layout.
        layout.addWidget(QLabel("Function of X:"),0,0)
        layout.addWidget(self.txtEquation,0,1)
        
        layout.addWidget(QLabel("Minimum Value of X:"),1,0)
        layout.addWidget(self.txtMinimumX,1,1)
        
        layout.addWidget(QLabel("Maximum Value of X:"),2,0)
        layout.addWidget(self.txtMaximumX,2,1)
        
        layout.addWidget(self.btnPlot,3,0, 2, 2)

        # Connecting the plot button to a function that plots the equation when the button is clicked.
        self.btnPlot.clicked.connect(self.plot)

        # Creating the plot figure and canvas.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Adding the canvas to the container layout.
        layout.addWidget(self.canvas, 6,0,6,2)


    def plot(self):
        # Clearing the previous plot.
        self.figure.clear()

        # Checking if the user provided all required inputs.
        self.validateUserInputs()

        # Validating the user-entered function, min value, and max value of X.
        function = self.validateFunction(self.txtEquation.text())
        minValue = self.validateUserInput(self.txtMinimumX.text())
        maxValue = self.validateUserInput(self.txtMaximumX.text())

        # Generating x values between min and max.
        try:
            x = np.linspace(minValue, maxValue, 100)
        except Exception as e:
            return

        # Plotting the function
        try:
            expr = sp.sympify(function)

        # Create a lambda function to evaluate the expression
            f = sp.lambdify(sp.symbols('x'), expr)

        # Evaluate the function for the given x values
            y = f(x)
        except Exception as e:
        # Handle the exception
            return
        axes = self.figure.add_subplot(111)
        axes.plot(x, y)
        axes.grid(True)
        
        self.canvas.draw()


    def validateUserInputs(self):
        '''Checks if the user provided all required inputs, and if not shows a MessageBox with the specific field not provided.'''

        if not self.txtEquation.text():
            QMessageBox.critical(self, "Missing Input", f"Missing Input: Please provide the function you want to plot.")
        elif not self.txtMinimumX.text():
            QMessageBox.critical(self, "Missing Input", f"Missing Input: Please provide the minimum value of X.")
        elif not self.txtMaximumX.text():
            QMessageBox.critical(self, "Missing Input", f"Missing Input: Please provide the maximum value of X.")
        
        return


    def validateFunction(self, function):
        # Removing whitespaces from the funcion (f(x)).
        function = "".join(function.split())
        
        # Replacing (**) with (^) to support this format (x^2).
        function = function.replace("^", "**")

        # Using regular expressions to check if the function (f(x)) contains unsupported operators.
        regex = re.compile('[^0-9xX\\+\\-\\*\\/\\^sincoletcg\\(\\)]+')
        match = regex.search(function)
        if match:
            unsupportedOperator = match.group()
            QMessageBox.critical(self, "Invalid Function", f"Invalid function. Unsupported operator found: {unsupportedOperator}")
        else:
            return function


    def validateUserInput(self,value):
        if not value:
            return

        try:
            value = float(value)
            return value
        except Exception as e:
            QMessageBox.critical(self, "Invalid Input", "Invalid Input: Please provide a number for X not letters.")
            return

        
if __name__ == "__main__":
  main()
        