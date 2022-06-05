from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtWidgets import QMenu, QLineEdit, QTabBar, QTabWidget,QMainWindow,QApplication,QToolBar,QAction
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem, QWebEnginePage,QWebEngineView
from functools import partial
import sys

class BrowserTabs(QMainWindow):

    Number_of_Tabs=1
    HomePage="https://www.google.co.in/"

    def __init__(self):
        '''
        Initialising the Browser
        '''
        super(BrowserTabs, self).__init__()

        # Initialising the Tabs - Document Mode, Accepting Drag Drop, Font Size and Allowing Close
        self.tabs=QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.setFont(QFont("",14))
        
        # Adding functionalities to the Tab
        self.tabs.tabBarDoubleClicked.connect(self.createNewTab)
        self.tabs.tabCloseRequested.connect(self.closeTab)

        self.navigationbar=QToolBar("Navigation Bar")
        self.navigationbar.isMovable()
        self.addToolBar(self.navigationbar)
        self.createNewTab()


        # Creating the Back Button and setting icon
        self.backbutton=QAction('Back',parent=self)
        self.backbutton.setIcon(QIcon('icons/Back.png'))

        # Providing the back functionality  to the button and  adding it to the window
        self.backbutton.triggered.connect(self.tabs.currentWidget().back)
        self.navigationbar.addAction(self.backbutton)

        # Creating the Forward Button and setting icon
        self.forwardbutton=QAction('Forward',parent=self)
        self.forwardbutton.setIcon(QIcon('icons/Forward.png'))

        # Providing the forward functionality  to the button and  adding it to the window
        self.forwardbutton.triggered.connect(self.moveForward)
        self.navigationbar.addAction(self.forwardbutton)

        # Creating the Reload Button and setting icon
        self.reloadbutton=QAction('Reload',parent=self)
        self.reloadbutton.setIcon(QIcon('icons/Reload.png'))

        # Providing the forward functionality  to the button and  adding it to the window
        self.reloadbutton.triggered.connect(self.tabs.currentWidget().reload)
        self.navigationbar.addAction(self.reloadbutton)

        # Creating the Search Bar and setting font to 14
        self.search_bar=QLineEdit()
        self.search_bar.setFont(QFont("",14))

        # Adding functionality when enter is pressed and adding the Search bar to navigation bar
        self.search_bar.returnPressed.connect(self.goto_url)
        self.navigationbar.addWidget(self.search_bar)

        # Telling the browser to change the website when ENTER is pressed (in Search Bar)
        self.tabs.currentWidget().urlChanged.connect(self.updateurl)

        # Creating the Reload Button and setting icon
        self.homebutton=QAction('Home',parent=self)
        self.homebutton.setIcon(QIcon('icons/Home.png'))

        # Providing the forward functionality  to the button and  adding it to the window
        self.homebutton.triggered.connect(self.goto_home)
        self.navigationbar.addAction(self.homebutton)

        self.setCentralWidget(self.tabs)
        self.showMaximized()
        

    def moveForward(self):
        self.tabs.currentWidget().forward()
        self.tabs.setTabText(self.tabs.currentIndex(), self.browser.title())

    def closeTab(self):
        '''
        A Function which is used to close a Tab
        '''
        self.tabs.removeTab(self.tabs.currentIndex())
        self.Number_of_Tabs-=1

    def updateurl(self,url):
        '''
        Making this function for updating the url in the search bar
        '''
        self.search_bar.setText(url.toString())
        self.tabs.setTabText(self.tabs.currentIndex(), self.browser.page().title())

    def goto_url(self):
        '''
        Making the goto_url function to get the url from the search bar and redirect to the webpage.
        '''
        url=self.search_bar.text()
        # print(self.browser.page().title())

        if url.startswith("file"):
            self.tabs.currentWidget().setUrl(QUrl(url))
            self.tabs.setTabText(self.tabs.currentIndex(), self.browser.page().title())

        else:
            self.tabs.currentWidget().setUrl(QUrl(url))
            self.tabs.setTabText(self.tabs.currentIndex(), self.browser.page().title())

    def goto_home(self):
        '''
        Making the Home Functionaity.
        '''
        self.tabs.currentWidget().setUrl(QUrl(self.HomePage))
        self.tabs.setTabText(self.tabs.currentIndex(), "Google")

    def createNewTab(self):
        '''
        A Function that is used to create a Tab.
        '''
        if self.Number_of_Tabs>=1:
            self.browser=QWebEngineView()
            self.tabs.addTab(self.browser,"New Tab")
            # self.search_bar.setText("")
            self.Number_of_Tabs+=1

        else:
            sys.exit(0)


if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setApplicationName('J.E.N Browser')
    window=BrowserTabs()
    app.exec_()

    