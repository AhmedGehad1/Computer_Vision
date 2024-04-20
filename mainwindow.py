# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6 import *
from PySide6.QtCore import Qt  # Import Qt module

from PySide6.QtCore import QPropertyAnimation, QSize
from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog


from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Computer Graphics")

        # Set the main background to transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        #top right corner buttons connections
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.Full_screen.clicked.connect(lambda: self.showMaximized())

        #hide_show Menu Button connector
        self.ui.Menu_slider.clicked.connect(lambda: self.hide_show())

        #combobox Connector
        self.ui.Selector_Method.currentIndexChanged.connect(lambda: self.handle_Selector_Method())

        #Image button Loader connection
        self.ui.Upload_Image.clicked.connect(lambda: self.load_image())


    #Load Image function
    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image files (*.jpg *.jpeg *.png *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)
            # if not pixmap.isNull():
            #     self.ui.Orginal.setPixmap(pixmap)
            # Scale the pixmap to 500x500 while preserving aspect ratio
            scaled_pixmap = pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.Orginal.setPixmap(scaled_pixmap)
        else:
            print("Failed to load image.")

    #Combobox choosing which detection we want 
    def handle_Selector_Method(self):
        index = self.ui.Selector_Method.currentIndex()
        if index == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page1)
        if index == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Page2)
        if index == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        
    #Hiding showing the side menu  
    def hide_show(self):
        # get current left menu
        width = self.ui.Slide_menu.width()
        if width == 0:
            newWidth = 220
        else:
            newWidth = 0
        #animation sidebar menu
        self.animation = QPropertyAnimation(self.ui.Slide_menu, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.start()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
