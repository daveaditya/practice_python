import sys
from PySide.QtGui import QApplication
from PySide.QtCore import QUrl
from PySide.QtWebKit import QWebPage
import bs4 as bs
import urllib.request


class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.app.quit()
        
url = 'http://products.amd.com/en-us/search?k=DesktopProcessors#k=DesktopProcessors'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
# soup = bs.BeautifulSoup(source, 'lxml')
print(source)
