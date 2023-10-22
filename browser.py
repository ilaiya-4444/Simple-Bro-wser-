import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))  # Set the initial webpage
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("SimpleWebBrowser")
    window = WebBrowser()
    app.exec_()
