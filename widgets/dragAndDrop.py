import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class ImageDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        
        self.urlFile = ""
        
        self.initComponents()
        
    def initComponents(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.label = QLabel("Drag and Drop Files here")
        self.label.setObjectName("dragAndDrop")
        self.label.setMinimumHeight(80)
        self.label.setMinimumWidth(200)
        
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        for url in event.mimeData().urls():

            image_path = url.toLocalFile()
            self.urlFile = image_path
            
            if image_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                pixmap = QPixmap(image_path)
                
                self.label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
                self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                event.accept()
                
                return
        
        event.ignore()
    
    def getUrlFile(self):
        return self.urlFile
        