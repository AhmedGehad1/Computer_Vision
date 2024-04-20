# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formKPwfCW.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)
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
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.Upload_Image = QPushButton(self.frame_6)
        self.Upload_Image.setObjectName(u"Upload_Image")
        self.Upload_Image.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Upload_Image.setIcon(icon)
        self.Upload_Image.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.Upload_Image, 0, 0, 1, 1)

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
        font2 = QFont()
        font2.setPointSize(12)
        self.Selector_Method.setFont(font2)

        self.gridLayout.addWidget(self.Selector_Method, 1, 0, 1, 2)

        self.stackedWidget = QStackedWidget(self.frame_6)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setStyleSheet(u"QLineEdit{\n"
" background-color: white;\n"
"}")
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
        self.formLayout = QFormLayout(self.frame_5)
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(11)
        self.label_4.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.Sigma = QLineEdit(self.frame_5)
        self.Sigma.setObjectName(u"Sigma")
        self.Sigma.setCursor(QCursor(Qt.PointingHandCursor))
        self.Sigma.setAutoFillBackground(False)
        self.Sigma.setStyleSheet(u"*{\n"
" background-color: white;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Sigma)

        self.Kernal = QLineEdit(self.frame_5)
        self.Kernal.setObjectName(u"Kernal")
        self.Kernal.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Kernal)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.T1 = QLineEdit(self.frame_5)
        self.T1.setObjectName(u"T1")
        self.T1.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.T1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.T2 = QLineEdit(self.frame_5)
        self.T2.setObjectName(u"T2")
        self.T2.setCursor(QCursor(Qt.PointingHandCursor))
        self.T2.setAutoFillBackground(False)
        self.T2.setStyleSheet(u"*{\n"
"	color:black;\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.T2)

        self.Empty = QLabel(self.frame_5)
        self.Empty.setObjectName(u"Empty")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.Empty)

        self.Submit1 = QPushButton(self.frame_5)
        self.Submit1.setObjectName(u"Submit1")
        self.Submit1.setFont(font2)
        self.Submit1.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Submit1.setIcon(icon1)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.Submit1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.label_8 = QLabel(self.Page2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 90, 49, 16))
        self.stackedWidget.addWidget(self.Page2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 130, 49, 16))
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
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setStrikeOut(False)
        self.label_10.setFont(font4)
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
        font5 = QFont()
        font5.setBold(False)
        font5.setKerning(False)
        self.Orginal.setFont(font5)
        self.Orginal.setCursor(QCursor(Qt.CrossCursor))
        self.Orginal.setScaledContents(False)

        self.horizontalLayout_7.addWidget(self.Orginal)

        self.Processed = QLabel(self.frame_8)
        self.Processed.setObjectName(u"Processed")
        self.Processed.setEnabled(True)
        font6 = QFont()
        font6.setKerning(False)
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.Upload_Image.setText("")
        self.Selector_Method.setItemText(0, QCoreApplication.translate("MainWindow", u"Canny Edge Detection", None))
        self.Selector_Method.setItemText(1, QCoreApplication.translate("MainWindow", u"Hough Line", None))
        self.Selector_Method.setItemText(2, QCoreApplication.translate("MainWindow", u"Harris Corner Detection", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sigma", None))
        self.Sigma.setText(QCoreApplication.translate("MainWindow", u"crcv", None))
        self.Kernal.setText(QCoreApplication.translate("MainWindow", u"egferg4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"T1", None))
        self.T1.setText(QCoreApplication.translate("MainWindow", u"efefegfr", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"T2", None))
        self.T2.setText(QCoreApplication.translate("MainWindow", u"efefef4", None))
        self.Empty.setText("")
        self.Submit1.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Kernal", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"whatever", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TRYY", None))
        self.Menu_slider.setText("")
        self.minimize_window_button.setText("")
        self.Full_screen.setText("")
        self.close_window_button.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Orginal Image", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Processed Image", None))
        self.Orginal.setText("")
        self.Processed.setText("")
    # retranslateUi

