# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './letterBoxApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox2.setObjectName("groupBox2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gb2_comboBox_A = QtWidgets.QComboBox(self.groupBox2)
        self.gb2_comboBox_A.setObjectName("gb2_comboBox_A")
        self.horizontalLayout_2.addWidget(self.gb2_comboBox_A)
        self.gb2_comboBox_B = QtWidgets.QComboBox(self.groupBox2)
        self.gb2_comboBox_B.setObjectName("gb2_comboBox_B")
        self.horizontalLayout_2.addWidget(self.gb2_comboBox_B)
        self.gb2_comboBox_C = QtWidgets.QComboBox(self.groupBox2)
        self.gb2_comboBox_C.setObjectName("gb2_comboBox_C")
        self.horizontalLayout_2.addWidget(self.gb2_comboBox_C)
        self.gridLayout.addWidget(self.groupBox2, 2, 2, 1, 1)
        self.groupBox4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox4.setObjectName("groupBox4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gb4_comboBox_A = QtWidgets.QComboBox(self.groupBox4)
        self.gb4_comboBox_A.setObjectName("gb4_comboBox_A")
        self.horizontalLayout.addWidget(self.gb4_comboBox_A)
        self.gb4_comboBox_B = QtWidgets.QComboBox(self.groupBox4)
        self.gb4_comboBox_B.setObjectName("gb4_comboBox_B")
        self.horizontalLayout.addWidget(self.gb4_comboBox_B)
        self.gb4_comboBox_C = QtWidgets.QComboBox(self.groupBox4)
        self.gb4_comboBox_C.setObjectName("gb4_comboBox_C")
        self.horizontalLayout.addWidget(self.gb4_comboBox_C)
        self.gridLayout.addWidget(self.groupBox4, 4, 2, 1, 1)
        self.groupBox1 = QtWidgets.QGroupBox(self.frame)
        self.groupBox1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox1.setObjectName("groupBox1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gb1_comboBox_A = QtWidgets.QComboBox(self.groupBox1)
        self.gb1_comboBox_A.setObjectName("gb1_comboBox_A")
        self.verticalLayout_2.addWidget(self.gb1_comboBox_A)
        self.gb1_comboBox_B = QtWidgets.QComboBox(self.groupBox1)
        self.gb1_comboBox_B.setObjectName("gb1_comboBox_B")
        self.verticalLayout_2.addWidget(self.gb1_comboBox_B)
        self.gb1_comboBox_C = QtWidgets.QComboBox(self.groupBox1)
        self.gb1_comboBox_C.setObjectName("gb1_comboBox_C")
        self.verticalLayout_2.addWidget(self.gb1_comboBox_C)
        self.gridLayout.addWidget(self.groupBox1, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.groupBox3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox3.setObjectName("groupBox3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb3_comboBox_A = QtWidgets.QComboBox(self.groupBox3)
        self.gb3_comboBox_A.setObjectName("gb3_comboBox_A")
        self.verticalLayout.addWidget(self.gb3_comboBox_A)
        self.gb3_comboBox_B = QtWidgets.QComboBox(self.groupBox3)
        self.gb3_comboBox_B.setObjectName("gb3_comboBox_B")
        self.verticalLayout.addWidget(self.gb3_comboBox_B)
        self.gb3_comboBox_C = QtWidgets.QComboBox(self.groupBox3)
        self.gb3_comboBox_C.setObjectName("gb3_comboBox_C")
        self.verticalLayout.addWidget(self.gb3_comboBox_C)
        self.gridLayout.addWidget(self.groupBox3, 3, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 4, 1, 1)
        self.lb_label = QtWidgets.QLabel(self.frame)
        self.lb_label.setStyleSheet("background-color: rgb(237, 51, 59);")
        self.lb_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_label.setObjectName("lb_label")
        self.gridLayout.addWidget(self.lb_label, 0, 0, 1, 5)
        self.wl_frame = QtWidgets.QFrame(self.splitter)
        self.wl_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.wl_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.wl_frame.setObjectName("wl_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wl_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wl_label = QtWidgets.QLabel(self.wl_frame)
        self.wl_label.setStyleSheet("background-color: rgb(255, 163, 72);")
        self.wl_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wl_label.setObjectName("wl_label")
        self.verticalLayout_3.addWidget(self.wl_label)
        self.wl_listWidget = QtWidgets.QListWidget(self.wl_frame)
        self.wl_listWidget.setObjectName("wl_listWidget")
        self.verticalLayout_3.addWidget(self.wl_listWidget)
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.solution_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.solution_label.setFont(font)
        self.solution_label.setStyleSheet("background-color: rgb(143, 240, 164);")
        self.solution_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.solution_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.solution_label.setObjectName("solution_label")
        self.verticalLayout_4.addWidget(self.solution_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.solution_add_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.solution_add_lineEdit.setObjectName("solution_add_lineEdit")
        self.horizontalLayout_3.addWidget(self.solution_add_lineEdit)
        self.solution_rmv_pb = QtWidgets.QPushButton(self.widget)
        self.solution_rmv_pb.setObjectName("solution_rmv_pb")
        self.horizontalLayout_3.addWidget(self.solution_rmv_pb)
        self.solution_add_pb = QtWidgets.QPushButton(self.widget)
        self.solution_add_pb.setObjectName("solution_add_pb")
        self.horizontalLayout_3.addWidget(self.solution_add_pb)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.generate_pb = QtWidgets.QPushButton(self.widget)
        self.generate_pb.setObjectName("generate_pb")
        self.verticalLayout_4.addWidget(self.generate_pb)
        self.verticalLayout_5.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox2.setTitle(_translate("MainWindow", "Group2"))
        self.groupBox4.setTitle(_translate("MainWindow", "Group4"))
        self.groupBox1.setTitle(_translate("MainWindow", "Group1"))
        self.groupBox3.setTitle(_translate("MainWindow", "Group3"))
        self.lb_label.setText(_translate("MainWindow", "Letter Box"))
        self.wl_label.setText(_translate("MainWindow", "WORDS LIST"))
        self.solution_label.setText(_translate("MainWindow", "Solution:"))
        self.solution_rmv_pb.setText(_translate("MainWindow", "-"))
        self.solution_add_pb.setText(_translate("MainWindow", "+"))
        self.generate_pb.setText(_translate("MainWindow", "GENERATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
