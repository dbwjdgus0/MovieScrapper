import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import infocrawl

class test(QMainWindow):
    def __init__(self, code):
        super().__init__()
        self.code= str(code)
        self.initUI(code)

    def initUI(self, code):
        self.label = QLabel(self)
        self.label.resize(300,300)

        ob = infocrawl.infoCrawl(code)
        url = ob.getImgurl()

        img = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(img)
        pixmap.scaledToWidth(300)
        self.label.setPixmap(pixmap)
        self.resize(500,500)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = test(17159)
    sys.exit(app.exec_())