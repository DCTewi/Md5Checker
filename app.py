"""
Application Entrance
"""

# coding=utf-8

import sys
import func.widgets
from static.style import stylesheets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    app.setFont(QFont('Consolas', 10))
    app.setStyleSheet(stylesheets)

    wid = func.widgets.MainWindow()
    wid.show()
    app.exec()


if __name__ == "__main__":
    main()
