from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFrame,
    QGridLayout,
    QWidget,
)
from modules.Convertir import convert_to_icon
from PyQt5.QtCore import (
    QFile,
    Qt
)
from PyQt5.QtGui import (
    QIcon,
    QPainter,
    QRegion,
    QPainterPath
)
from PyQt5.uic import loadUi
from os import (
    getcwd,
    environ
)
from os.path import (
    join,
    dirname
)

from widgets.dragAndDrop import ImageDropWidget

import sys

class Main(QMainWindow):
    
    def __init__(self):
        self.rootPath = getcwd()
        self.uiPath = join(self.rootPath, "ui", "Interface.ui")
        
        QMainWindow.__init__(self)
        loadUi(self.uiPath,self)
        
        self.initComponents()

    def initComponents(self):
        self.styleElements()
        
        self.SameLocation.triggered.connect(self.sameLocation)
        self.SelectLocation.triggered.connect(self.selectLocation)
        self.btn_convert.clicked.connect(self.Convertir)
        
        self.widgetDrag = ImageDropWidget()
        frame = self.findChild(QFrame, "frame_3")
        splitleft = QWidget()
        splitright = QWidget()
        
        for child in frame.children():
            if child.objectName() == "spacer_left":
                splitleft = child
            elif child.objectName() == "spacer_right":
                splitright = child
        
        gridLayout = QGridLayout()
        frame.setLayout(gridLayout)
        gridLayout.addWidget(splitleft, 0, 0)
        gridLayout.addWidget(self.widgetDrag, 0, 1)
        gridLayout.addWidget(splitright, 0, 2)
        
        self.appIcon = QIcon(join(self.rootPath, "img", "Mi_Logo.ico"))
        self.setWindowIcon(self.appIcon)
        
        self.setWindowTitle("Image To Icon")
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.pathImages = join(self.rootPath, "img")
       
        settingIco = QIcon(join(self.pathImages, "settings.png"))
        setPathIco = QIcon(join(self.pathImages, "setFolder.png"))
        currentPathIco = QIcon(join(self.pathImages, "currentFolder.png"))

        menuSettings = self.menuSettings
        esto = QWidget()
        for item in menuSettings.children():
            if item.objectName() == "menuOutput_Path":
                item.setIcon(settingIco)
                esto = item
        for childItmem in esto.children():
            if childItmem.objectName() == "SameLocation":
                childItmem.setIcon(currentPathIco)
            elif childItmem.objectName() == "SelectLocation":
                childItmem.setIcon(setPathIco)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 10, 10)

        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

    def styleElements(self):
        try:
            file = QFile(join(self.rootPath, "styles", "style.css"))
            file.open(QFile.ReadOnly)
            style = str(file.readAll(),encoding="utf-8")
            
            self.setStyleSheet(style)
        except:
            print("Error leyendo los estilos")
            
    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Escape:
            self.close()
            event.accept()
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
            
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
            
    def Convertir(self):
        print("Convirtiendo")
        
        urlFIle = self.widgetDrag.getUrlFile()
        
        path_out = "D:/salida.ico"
        print(dirname(urlFIle))

        convert_to_icon(urlFIle, path_out)

    def sameLocation(self):
        print("Hola Mundo")
        variable = environ.get("ItI-Config")
        print(variable)
        if variable == None:
            print("No se ha creado la variable... Crando....")
            environ.setdefault("ItI-Config", "Hola Mundo")
        else:
            print("Obteniendo Valor de variable")
            variable = environ.get("ItI-Config")
            
    
    def selectLocation(self):
        print("Localizando")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())