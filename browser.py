import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class  Browser(QMainWindow):
    def __init__(self):
        super(Browser,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.co.in/"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.navbar=QToolBar()
        self.addToolBar(self.navbar)
        self.backbutton=QAction('Back',parent=self)
        self.backbutton.setIcon(QIcon('Back.png'))
        self.backbutton.triggered.connect(self.browser.back)
        self.navbar.addAction(self.backbutton)
        self.forwardbutton=QAction('Forward',parent=self)
        self.forwardbutton.setIcon(QIcon('Forward.png'))
        self.forwardbutton.triggered.connect(self.browser.forward)
        self.navbar.addAction(self.forwardbutton)
        self.reloadbutton=QAction('Reload',parent=self)
        self.reloadbutton.setIcon(QIcon('Reload.png'))
        self.reloadbutton.triggered.connect(self.browser.reload)
        self.navbar.addAction(self.reloadbutton)
        self.search_bar=QLineEdit()
        self.search_bar.returnPressed.connect(self.goto_url)
        self.navbar.addWidget(self.search_bar)
        self.browser.urlChanged.connect(self.updateurl)
        self.homebutton=QAction('Home',parent=self)
        self.homebutton.setIcon(QIcon('Home.png'))
        self.homebutton.triggered.connect(self.goto_home)
        self.navbar.addAction(self.homebutton)
    def goto_home(self):
        self.browser.setUrl(QUrl("http://www.google.co.in/"))
    def goto_url(self):
        url=self.search_bar.text()
        self.browser.setUrl(QUrl(url))
    def updateurl(self,url):
        self.search_bar.setText(url.toString())
if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setApplicationName('J.E.N Browser')
    app.setWindowIcon(QIcon('JEN.png'))
    window=Browser()
    app.exec_()