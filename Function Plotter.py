import re
import sys
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox,QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide2.QtGui import QIcon


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
        self.setWindowIcon(QIcon("icon.png"))

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
        pass        

if __name__ == "__main__":
  main()
