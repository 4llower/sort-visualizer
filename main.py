from graphics import *
from mergeSort import mergeSorting
from bubbleSort import bubbleSorting
from quickSort import quickSorting
from drawing import Draw
import sys
from LSDsort import LSDsorting
from countSort import countSorting
import random
from PyQt5 import QtCore, QtGui, QtWidgets

# constants
Length = 600
Width = 1200
Stick_length = 2
ValueOfSicks = 600
white_color = color_rgb(255, 255, 255)
black_color = color_rgb(0, 0, 0)
# constants



class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Visual):
        self.Visual = Visual
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 90, 106, 190))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mergeSortButton = QtWidgets.QPushButton(self.widget)
        self.mergeSortButton.setObjectName("mergeSortButton")
        self.gridLayout.addWidget(self.mergeSortButton, 2, 0, 1, 1)
        self.StatisticsButton = QtWidgets.QPushButton(self.widget)
        self.StatisticsButton.setObjectName("StatisticsButton")
        self.gridLayout.addWidget(self.StatisticsButton, 6, 0, 1, 1)
        self.countSortButton = QtWidgets.QPushButton(self.widget)
        self.countSortButton.setObjectName("countSortButton")
        self.gridLayout.addWidget(self.countSortButton, 4, 0, 1, 1)
        self.bubbleSortButton = QtWidgets.QPushButton(self.widget)
        self.bubbleSortButton.setObjectName("bubbleSortButton")
        self.gridLayout.addWidget(self.bubbleSortButton, 5, 0, 1, 1)
        self.quickSortButton = QtWidgets.QPushButton(self.widget)
        self.quickSortButton.setObjectName("quickSortButton")
        self.gridLayout.addWidget(self.quickSortButton, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.quickSortButton.clicked.connect(self.make_quick_sort)
        self.mergeSortButton.clicked.connect(self.make_merge_sort)
        self.bubbleSortButton.clicked.connect(self.make_bubble_sort)
        self.countSortButton.clicked.connect(self.make_count_sort)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sort Vizualiser"))
        self.mergeSortButton.setText(_translate("MainWindow", "Merge sort"))
        self.StatisticsButton.setText(_translate("MainWindow", "Statistics"))
        self.countSortButton.setText(_translate("MainWindow", "Count sort"))
        self.bubbleSortButton.setText(_translate("MainWindow", "Bubble sort"))
        self.quickSortButton.setText(_translate("MainWindow", "Quick sort"))

    def createWindow(self):
        self.Visual.canvas = GraphWin("Sort visualize", Width, Length)
        self.Visual.canvas.setBackground(black_color)

    def shuffling(self):
        random.shuffle(self.Visual.array)
        self.Visual.creating_retangles()

    def end_sorting(self):
        self.Visual.complete()
        self.Visual.canvas.close()

    def make_merge_sort(self):
        self.Visual.delay = 0
        self.createWindow()
        self.shuffling()
        try:
            mergeSorting(self.Visual, 0, len(self.Visual.array) - 1)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_quick_sort(self):
        self.Visual.delay = 0.01
        self.createWindow()
        self.shuffling()
        try:
            quickSorting(self.Visual, 0, len(self.Visual.array) - 1)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_count_sort(self):
        self.Visual.delay = 0.01
        self.createWindow()
        self.shuffling()
        try:
            countSorting(self.Visual)
        except GraphicsError:
            pass
        self.end_sorting()

    def make_bubble_sort(self):
        self.Visual.delay = 0
        self.createWindow()
        self.shuffling()
        try:
            bubbleSorting(self.Visual)
        except GraphicsError:
            pass
        self.end_sorting()

def main():

    try:

        temp = [i for i in range(1, ValueOfSicks)]
        Visual = Draw(Length, Width, Stick_length, 0, white_color, black_color, temp, 0)

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow, Visual)
        MainWindow.show()
        sys.exit(app.exec_())

    except GraphicsError:
        print("Success")


if (__name__ == "__main__"):
    main()