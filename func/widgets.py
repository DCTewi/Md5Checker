"""
Tool Widget
"""

# coding=utf-8

import base64
import func.utils
import static.logo
from PyQt5.QtGui import (
    QIcon,
    QPixmap,
)
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QFileDialog,
    QPushButton,
    QLineEdit,
    QPlainTextEdit,
    QLabel,
)


class MainWindow(QMainWindow):
    check_path = ''
    raw_md5 = ''
    res_md5 = ''

    def __init__(self):
        super().__init__()

        self.path_label = QLabel('Path:', self)
        self.path_edit = QPlainTextEdit(self)
        self.path_browse = QPushButton('Browse', self)
        self.raw_label = QLabel('Target MD5:', self)
        self.raw_edit = QLineEdit(self)
        self.res_label = QLabel('Result MD5:', self)
        self.res_edit = QLineEdit(self)
        self.check_button = QPushButton('Check', self)

        self.init_ui()

    def init_ui(self):
        # config
        self.path_edit.setFixedHeight(self.raw_edit.height())
        self.path_edit.setAcceptDrops(True)
        self.path_edit.textChanged.connect(self.drop_rename)
        self.path_browse.clicked.connect(self.browse_file)
        self.res_edit.setReadOnly(True)
        self.check_button.clicked.connect(self.sum_md5)

        # placement
        grid = QGridLayout()
        grid.addWidget(self.path_label, 1, 0)
        grid.addWidget(self.path_edit, 1, 1)
        grid.addWidget(self.path_browse, 1, 2)
        grid.addWidget(self.raw_label, 2, 0)
        grid.addWidget(self.raw_edit, 2, 1)
        grid.addWidget(self.res_label, 3, 0)
        grid.addWidget(self.res_edit, 3, 1)
        grid.addWidget(self.check_button, 3, 2)

        widget = QWidget(self)
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        rawimg = base64.b64decode(static.logo.icon)
        pix = QPixmap()
        pix.loadFromData(rawimg)
        icon = QIcon()
        icon.addPixmap(pix, QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('md5checker')

        self.statusBar().showMessage('Ready')

    def drop_rename(self):
        if 0 == self.path_edit.toPlainText().find('file:///'):
            self.path_edit.setPlainText(
                self.path_edit.toPlainText().replace('file:///', ''))
            self.update_file_path(self.path_edit.toPlainText())

    def browse_file(self):
        path = QFileDialog.getOpenFileName(self, directory='/')
        self.update_file_path(path[0])

    def update_file_path(self, newpath: str):
        self.check_path = newpath
        self.path_edit.setPlainText(newpath)

    def sum_md5(self):
        res = ''
        try:
            res = func.utils.get_sum_md5(self.path_edit.toPlainText())
            self.raw_md5 = self.raw_edit.text()
            if self.raw_md5 != '':
                if self.raw_md5 == res:
                    self.statusBar().showMessage('Correct')
                else:
                    self.statusBar().showMessage('Wrong')
            else:
                self.statusBar().showMessage('Got result')
            self.res_edit.setText(res)
        except Exception as err:
            self.statusBar().showMessage(str(err))
