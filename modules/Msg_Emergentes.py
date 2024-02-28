from PyQt5.QtWidgets import (
    QDialog,
    QLabel
)
from PyQt5.QtCore import (
    Qt
)
from PyQt5.QtGui import (
    QIcon
)
from os import (
    getcwd
)
from os.path import (
    join
)

class Messagge(QDialog):
    
    def __init__(self,msg, *args, **kwargs):
        
        super(QDialog, self).__init__(*args, **kwargs)

        self.msg = msg

        path_icon = join(getcwd(), "img", "Mi_Logo.ico")
        
        icon = QIcon(path_icon)
        
        self.setFixedSize(300,100)
        self.setWindowTitle("Information")
        self.setStyleSheet(
            """
                background-color: #202020;
            """
        )
        self.setWindowIcon(icon)
        self.setVisible(True)
        
        self.initComponents()
        
    def initComponents(self):
        self.label = QLabel(self.msg, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(
            """
                font-size: 15px;
                color: #0f0;
            """
        )
        self.label.setFixedSize(290, 100)
        self.label.setEnabled(True)
        self.label.setVisible(True)
        
if __name__ == "__main__":
    
    msg = Messagge()
    msg.show()
