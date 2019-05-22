#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Filename: test1.py
@version: v1.0 
@author: WeWe
@Time: 2019/5/22 10:04
@Last Modified time: 2019/5/22 10:04
@Explain: This file is for ...
"""

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys


class MyWebEngineView(QWebEngineView):
    windowList = []

    def createWindow(self, QWebEnginePage_WebWindowType):
        new_web_view = MyWebEngineView()
        new_window = WebEngineView()
        new_window.setCentralWidget(new_web_view)
        new_window.show()
        self.windowList.append(new_window)

        return new_web_view


class WebEngineView(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WebEngineView, self).__init__(*args, **kwargs)
        self.setWindowTitle("打开外部网页")
        self.setGeometry(5, 30, 1300, 700)
        self.browser = MyWebEngineView()
        self.browser.load(QUrl("https://www.hao123.com"))
        self.setCentralWidget(self.browser)


def main():
    app = QApplication(sys.argv)
    win = WebEngineView()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    pass
