# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formbPoHmP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(786, 463)
        MainWindow.setMaximumSize(QSize(1900, 1000))
        MainWindow.setStyleSheet(u"*{\n"
" boarder:none;\n"
"color:white;\n"
"}\n"
"QLineEdit{\n"
" border: 4px solid;\n"
" background-color: white;\n"
" boarder-radius: 20px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setStyleSheet(u"background-color:rgb(24, 24, 36);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Slide_menu = QFrame(self.centralwidget)
        self.Slide_menu.setObjectName(u"Slide_menu")
        self.Slide_menu.setMaximumSize(QSize(220, 16777215))
        self.Slide_menu.setStyleSheet(u"background-color:rgb(9,5,13);")
        self.Slide_menu.setFrameShape(QFrame.StyledPanel)
        self.Slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Slide_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Slide_menu)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 9, 20)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/icons/camera.svg"))

        self.horizontalLayout_5.addWidget(self.label, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Selector_Method = QComboBox(self.frame_6)
        self.Selector_Method.addItem("")
        self.Selector_Method.addItem("")
        self.Selector_Method.addItem("")
        self.Selector_Method.setObjectName(u"Selector_Method")
        self.Selector_Method.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(30)
        sizePolicy2.setHeightForWidth(self.Selector_Method.sizePolicy().hasHeightForWidth())
        self.Selector_Method.setSizePolicy(sizePolicy2)
        self.Selector_Method.setMinimumSize(QSize(0, 30))
        self.Selector_Method.setFont(font)

        self.gridLayout.addWidget(self.Selector_Method, 1, 0, 1, 2)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.Upload_Image = QPushButton(self.frame_6)
        self.Upload_Image.setObjectName(u"Upload_Image")
        font1 = QFont()
        font1.setPointSize(15)
        self.Upload_Image.setFont(font1)
        self.Upload_Image.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Upload_Image.setIcon(icon)
        self.Upload_Image.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.Upload_Image, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.frame_6)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setStyleSheet(u"QLineEdit{\n"
" background-color: white;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"}\n"
"QPushButton{\n"
"background-color: #333333;\n"
"border-radius: 10px;\n"
"}")
        self.stackedWidget.setLocale(QLocale(QLocale.English, QLocale.Zimbabwe))
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_4 = QVBoxLayout(self.page1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.page1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QLineEdit{\n"
"	color: black;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Kernal = QLineEdit(self.frame_5)
        self.Kernal.setObjectName(u"Kernal")
        self.Kernal.setCursor(QCursor(Qt.IBeamCursor))
        self.Kernal.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout_2.addWidget(self.Kernal, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_4.setFont(font2)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.Sigma = QLineEdit(self.frame_5)
        self.Sigma.setObjectName(u"Sigma")
        self.Sigma.setCursor(QCursor(Qt.IBeamCursor))
        self.Sigma.setAutoFillBackground(False)
        self.Sigma.setStyleSheet(u"*{\n"
" background-color: white;\n"
"}")
        self.Sigma.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout_2.addWidget(self.Sigma, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_6.setFont(font3)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.T1 = QLineEdit(self.frame_5)
        self.T1.setObjectName(u"T1")
        self.T1.setCursor(QCursor(Qt.IBeamCursor))
        self.T1.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout_2.addWidget(self.T1, 2, 1, 1, 1)

        self.T2 = QLineEdit(self.frame_5)
        self.T2.setObjectName(u"T2")
        self.T2.setCursor(QCursor(Qt.IBeamCursor))
        self.T2.setAutoFillBackground(False)
        self.T2.setStyleSheet(u"*{\n"
"	color:black;\n"
"}")
        self.T2.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout_2.addWidget(self.T2, 3, 1, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.Submit1 = QPushButton(self.frame_5)
        self.Submit1.setObjectName(u"Submit1")
        self.Submit1.setFont(font3)
        self.Submit1.setCursor(QCursor(Qt.PointingHandCursor))
        self.Submit1.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Submit1.setIcon(icon1)

        self.gridLayout_2.addWidget(self.Submit1, 4, 0, 1, 3)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.gridLayout_6 = QGridLayout(self.Page2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_10 = QFrame(self.Page2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QLineEdit{\n"
"	color: black;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Threshold_Max = QLineEdit(self.frame_10)
        self.Threshold_Max.setObjectName(u"Threshold_Max")
        self.Threshold_Max.setCursor(QCursor(Qt.IBeamCursor))
        self.Threshold_Max.setAutoFillBackground(False)
        self.Threshold_Max.setStyleSheet(u"*{\n"
"	color:black;\n"
"}")
        self.Threshold_Max.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout_5.addWidget(self.Threshold_Max, 0, 1, 1, 1)

        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")
        font4 = QFont()
        font4.setPointSize(13)
        self.label_13.setFont(font4)

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.Submit_Hough_line = QPushButton(self.frame_10)
        self.Submit_Hough_line.setObjectName(u"Submit_Hough_line")
        self.Submit_Hough_line.setFont(font3)
        self.Submit_Hough_line.setCursor(QCursor(Qt.PointingHandCursor))
        self.Submit_Hough_line.setStyleSheet(u"")
        self.Submit_Hough_line.setIcon(icon1)

        self.gridLayout_5.addWidget(self.Submit_Hough_line, 2, 0, 1, 3)

        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.Resolution = QLineEdit(self.frame_10)
        self.Resolution.setObjectName(u"Resolution")

        self.gridLayout_5.addWidget(self.Resolution, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Page2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QLineEdit{\n"
"	color: black;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.threshold_corner = QLineEdit(self.frame_9)
        self.threshold_corner.setObjectName(u"threshold_corner")
        self.threshold_corner.setCursor(QCursor(Qt.IBeamCursor))
        self.threshold_corner.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout_3.addWidget(self.threshold_corner, 1, 1, 1, 1)

        self.label_17 = QLabel(self.frame_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.gridLayout_3.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.window_size = QLineEdit(self.frame_9)
        self.window_size.setObjectName(u"window_size")
        self.window_size.setCursor(QCursor(Qt.IBeamCursor))
        self.window_size.setAutoFillBackground(False)
        self.window_size.setStyleSheet(u"*{\n"
" background-color: white;\n"
"}")
        self.window_size.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout_3.addWidget(self.window_size, 0, 1, 1, 1)

        self.Submit_corner = QPushButton(self.frame_9)
        self.Submit_corner.setObjectName(u"Submit_corner")
        self.Submit_corner.setFont(font3)
        self.Submit_corner.setCursor(QCursor(Qt.PointingHandCursor))
        self.Submit_corner.setStyleSheet(u"")
        self.Submit_corner.setIcon(icon1)

        self.gridLayout_3.addWidget(self.Submit_corner, 2, 0, 1, 3)


        self.gridLayout_4.addWidget(self.frame_9, 0, 0, 2, 2)

        self.stackedWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.Slide_menu)

        self.mainbody = QFrame(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        self.mainbody.setFrameShape(QFrame.StyledPanel)
        self.mainbody.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainbody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.mainbody)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"background-color:rgb(9,5,13)")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Menu_slider = QPushButton(self.frame_2)
        self.Menu_slider.setObjectName(u"Menu_slider")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_slider.setIcon(icon2)
        self.Menu_slider.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.Menu_slider)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame_3)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.Full_screen = QPushButton(self.frame_3)
        self.Full_screen.setObjectName(u"Full_screen")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Full_screen.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.Full_screen)

        self.close_window_button = QPushButton(self.frame_3)
        self.close_window_button.setObjectName(u"close_window_button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.body = QFrame(self.mainbody)
        self.body.setObjectName(u"body")
        sizePolicy1.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy1)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.body)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_7 = QFrame(self.body)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setStrikeOut(False)
        self.label_10.setFont(font5)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.body)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Orginal = QLabel(self.frame_8)
        self.Orginal.setObjectName(u"Orginal")
        self.Orginal.setMaximumSize(QSize(1900, 1080))
        font6 = QFont()
        font6.setKerning(False)
        self.Orginal.setFont(font6)
        self.Orginal.setCursor(QCursor(Qt.CrossCursor))
        self.Orginal.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.Orginal)

        self.Processed = QLabel(self.frame_8)
        self.Processed.setObjectName(u"Processed")
        self.Processed.setEnabled(True)
        self.Processed.setMaximumSize(QSize(1900, 1080))
        self.Processed.setFont(font6)
        self.Processed.setCursor(QCursor(Qt.CrossCursor))
        self.Processed.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.Processed)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.body)


        self.horizontalLayout.addWidget(self.mainbody)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 786, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Computer Vision ", None))
        self.label.setText("")
        self.Selector_Method.setItemText(0, QCoreApplication.translate("MainWindow", u"Canny Edge Detection", None))
        self.Selector_Method.setItemText(1, QCoreApplication.translate("MainWindow", u"Hough Line", None))
        self.Selector_Method.setItemText(2, QCoreApplication.translate("MainWindow", u"Harris Corner Detection", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.Upload_Image.setText("")
        self.Kernal.setText("")
        self.Kernal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kernal", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sigma", None))
        self.Sigma.setText("")
        self.Sigma.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sigma", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Threshold1", None))
        self.T1.setText("")
        self.T1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Threshold 1", None))
        self.T2.setText("")
        self.T2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Threshold 2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Threshold2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Kernal", None))
        self.Submit1.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.Threshold_Max.setText("")
        self.Threshold_Max.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Threshold 2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.Submit_Hough_line.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.Resolution.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.threshold_corner.setText("")
        self.threshold_corner.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Window size", None))
        self.window_size.setText("")
        self.window_size.setPlaceholderText(QCoreApplication.translate("MainWindow", u"window", None))
        self.Submit_corner.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.Menu_slider.setText("")
        self.minimize_window_button.setText("")
        self.Full_screen.setText("")
        self.close_window_button.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Orginal Image", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Processed Image", None))
        self.Orginal.setText("")
        self.Processed.setText("")
    # retranslateUi

