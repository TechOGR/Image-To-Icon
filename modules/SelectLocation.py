from PyQt5.QtWidgets import (
    QFileDialog
)
from os import getcwd

class DialogFile(QFileDialog):
    
    def __init__(self, *args, **kwargs):
        super(DialogFile, self).__init__(*args, **kwargs)
        
        self.setFileMode(QFileDialog.DirectoryOnly)
        self.setDirectory(getcwd())

        self.setWindowTitle("OutPut Folder")       
