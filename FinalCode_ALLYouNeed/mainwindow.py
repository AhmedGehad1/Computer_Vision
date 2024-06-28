import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6 import *
from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtGui import QPixmap, QIcon
from edge_detection_with_parameters import canny_edge_detection
from Hough import detect_lines
from Harris import my_harris
from ui_form import Ui_MainWindow

file_path = ""
New_file_path = ""
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

        # File path variable storage for images
        self.file_path = ""
        self.New_file_path = ""

        #Sumbit1 connection Canny Edge Detection
        self.ui.Submit1.clicked.connect(lambda: self.Submit_Canny())

        # Hough Line Sumbit Connection
        self.ui.Submit_Hough_line.clicked.connect(lambda: self.Submit_Hough_Line())

    #     # Harris Corner detection 
        self.ui.Submit_corner.clicked.connect(lambda: self.Submit_Harris_corner())

    
    def Submit_Harris_corner(self):
        a = float((self.ui.threshold_corner.text()))
        b = int(self.ui.window_size.text())
        #Must be =>3 and Odd window_size
        print(self.file_path)
        
        self.New_file_path = my_harris(self.file_path, a, b)

        # Load Processed Image
        if self.New_file_path:
            pixmap = QPixmap(self.New_file_path)
            scaled_pixmap = pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.Processed.setPixmap(scaled_pixmap)
        else:
            print("Failed to load image.")

    def Submit_Hough_Line(self):
        a = float(self.ui.Threshold_Max.text())
        b = int(self.ui.Resolution.text())
        
        # Hough Line
        self.New_file_path = detect_lines(self.file_path,a,b)

        # Load Processed Image
        if self.New_file_path:
            pixmap = QPixmap(self.New_file_path)
            scaled_pixmap = pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.Processed.setPixmap(scaled_pixmap)
        else:
            print("Failed to load image.")

    def Submit_Canny(self):
        # Canny input values
        a = float(self.ui.Sigma.text())
        b = int(self.ui.Kernal.text())
        c = float(self.ui.T1.text())
        d = float(self.ui.T2.text())

        # Canny edge detection
        print(self.file_path)
        self.New_file_path = canny_edge_detection( self.file_path,b,a ,c, d)
        print(self.New_file_path)

        # Load Processed Image
        if self.New_file_path:
            pixmap = QPixmap(self.New_file_path)
            scaled_pixmap = pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.Processed.setPixmap(scaled_pixmap)
        else:
            print("Failed to load image.")

    #Load Image function
    def load_image(self):

        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image files (*.jpg *.jpeg *.png *.bmp)")
        print("Selected file path:", self.file_path)

        if self.New_file_path != "":
        # Set the processed image label to be empty
            self.ui.Processed.clear()
        
        if self.file_path:
            pixmap = QPixmap(self.file_path)
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
