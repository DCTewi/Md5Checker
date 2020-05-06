"""
Entrance
"""

# coding=utf-8

import sys
import widgets
from style import stylesheets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont

def main():
    app = QApplication(sys.argv)
    app.setFont(QFont('Consolas', 10))
    app.setStyleSheet(stylesheets)

    wid = widgets.MainWindow()
    wid.show()
    app.exec()


if __name__ == "__main__":
    main()
