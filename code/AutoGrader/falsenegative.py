# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'falsenegative.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FalseNegativeWindow(object):
    def setupUi(self, FalseNegativeWindow):
        FalseNegativeWindow.setObjectName("FalseNegativeWindow")
        FalseNegativeWindow.resize(808, 611)
        self.centralwidget = QtWidgets.QWidget(FalseNegativeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 801, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(36)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(470, 210, 241, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.signCategories_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.signCategories_2.setContentsMargins(0, 0, 0, 0)
        self.signCategories_2.setObjectName("signCategories_2")
        self.regulatoryVBOX_2 = QtWidgets.QVBoxLayout()
        self.regulatoryVBOX_2.setObjectName("regulatoryVBOX_2")
        self.regulatoryContainer_2 = QtWidgets.QHBoxLayout()
        self.regulatoryContainer_2.setObjectName("regulatoryContainer_2")
        self.regulatorySign_2 = QtWidgets.QHBoxLayout()
        self.regulatorySign_2.setObjectName("regulatorySign_2")
        self.regulatoryLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.regulatoryLabel_2.setFont(font)
        self.regulatoryLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.regulatoryLabel_2.setObjectName("regulatoryLabel_2")
        self.regulatorySign_2.addWidget(self.regulatoryLabel_2)
        self.regulatoryContainer_2.addLayout(self.regulatorySign_2)
        self.regulatoryPercentage_2 = QtWidgets.QHBoxLayout()
        self.regulatoryPercentage_2.setObjectName("regulatoryPercentage_2")
        self.regulatoryPercentValue_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.regulatoryPercentValue_2.setFrameShape(QtWidgets.QFrame.Box)
        self.regulatoryPercentValue_2.setText("")
        self.regulatoryPercentValue_2.setObjectName("regulatoryPercentValue_2")
        self.regulatoryPercentage_2.addWidget(self.regulatoryPercentValue_2)
        self.regulatoryContainer_2.addLayout(self.regulatoryPercentage_2)
        self.regulatoryVBOX_2.addLayout(self.regulatoryContainer_2)
        self.signCategories_2.addLayout(self.regulatoryVBOX_2)
        self.guidingVBOX_2 = QtWidgets.QVBoxLayout()
        self.guidingVBOX_2.setObjectName("guidingVBOX_2")
        self.guidingContainer_2 = QtWidgets.QHBoxLayout()
        self.guidingContainer_2.setObjectName("guidingContainer_2")
        self.guidingSign_2 = QtWidgets.QHBoxLayout()
        self.guidingSign_2.setObjectName("guidingSign_2")
        self.guidingLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.guidingLabel_2.setFont(font)
        self.guidingLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.guidingLabel_2.setObjectName("guidingLabel_2")
        self.guidingSign_2.addWidget(self.guidingLabel_2)
        self.guidingContainer_2.addLayout(self.guidingSign_2)
        self.guidingPercentage_2 = QtWidgets.QHBoxLayout()
        self.guidingPercentage_2.setObjectName("guidingPercentage_2")
        self.guidingPercentValue_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.guidingPercentValue_2.setFrameShape(QtWidgets.QFrame.Box)
        self.guidingPercentValue_2.setText("")
        self.guidingPercentValue_2.setObjectName("guidingPercentValue_2")
        self.guidingPercentage_2.addWidget(self.guidingPercentValue_2)
        self.guidingContainer_2.addLayout(self.guidingPercentage_2)
        self.guidingVBOX_2.addLayout(self.guidingContainer_2)
        self.signCategories_2.addLayout(self.guidingVBOX_2)
        self.warningVBOX_2 = QtWidgets.QVBoxLayout()
        self.warningVBOX_2.setObjectName("warningVBOX_2")
        self.warningContainer_2 = QtWidgets.QHBoxLayout()
        self.warningContainer_2.setObjectName("warningContainer_2")
        self.warningSign_2 = QtWidgets.QHBoxLayout()
        self.warningSign_2.setObjectName("warningSign_2")
        self.warningLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.warningLabel_2.setFont(font)
        self.warningLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.warningLabel_2.setObjectName("warningLabel_2")
        self.warningSign_2.addWidget(self.warningLabel_2)
        self.warningContainer_2.addLayout(self.warningSign_2)
        self.warningPercentage_2 = QtWidgets.QHBoxLayout()
        self.warningPercentage_2.setObjectName("warningPercentage_2")
        self.warningPercentValue_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.warningPercentValue_2.setFrameShape(QtWidgets.QFrame.Box)
        self.warningPercentValue_2.setText("")
        self.warningPercentValue_2.setObjectName("warningPercentValue_2")
        self.warningPercentage_2.addWidget(self.warningPercentValue_2)
        self.warningContainer_2.addLayout(self.warningPercentage_2)
        self.warningVBOX_2.addLayout(self.warningContainer_2)
        self.signCategories_2.addLayout(self.warningVBOX_2)
        self.constructionVBOX_2 = QtWidgets.QVBoxLayout()
        self.constructionVBOX_2.setObjectName("constructionVBOX_2")
        self.constructionContainer_2 = QtWidgets.QHBoxLayout()
        self.constructionContainer_2.setObjectName("constructionContainer_2")
        self.constructionSign_2 = QtWidgets.QHBoxLayout()
        self.constructionSign_2.setObjectName("constructionSign_2")
        self.constructionLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.constructionLabel_2.setFont(font)
        self.constructionLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.constructionLabel_2.setObjectName("constructionLabel_2")
        self.constructionSign_2.addWidget(self.constructionLabel_2)
        self.constructionContainer_2.addLayout(self.constructionSign_2)
        self.constructionPercentage_2 = QtWidgets.QHBoxLayout()
        self.constructionPercentage_2.setObjectName("constructionPercentage_2")
        self.constructionPercentValue_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.constructionPercentValue_2.setFrameShape(QtWidgets.QFrame.Box)
        self.constructionPercentValue_2.setText("")
        self.constructionPercentValue_2.setObjectName("constructionPercentValue_2")
        self.constructionPercentage_2.addWidget(self.constructionPercentValue_2)
        self.constructionContainer_2.addLayout(self.constructionPercentage_2)
        self.constructionVBOX_2.addLayout(self.constructionContainer_2)
        self.signCategories_2.addLayout(self.constructionVBOX_2)
        self.otherVBOX_2 = QtWidgets.QVBoxLayout()
        self.otherVBOX_2.setObjectName("otherVBOX_2")
        self.otherContainer_2 = QtWidgets.QHBoxLayout()
        self.otherContainer_2.setObjectName("otherContainer_2")
        self.otherSign_2 = QtWidgets.QHBoxLayout()
        self.otherSign_2.setObjectName("otherSign_2")
        self.otherLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.otherLabel_2.setFont(font)
        self.otherLabel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.otherLabel_2.setObjectName("otherLabel_2")
        self.otherSign_2.addWidget(self.otherLabel_2)
        self.otherContainer_2.addLayout(self.otherSign_2)
        self.otherPercentage_2 = QtWidgets.QHBoxLayout()
        self.otherPercentage_2.setObjectName("otherPercentage_2")
        self.otherPercentValue_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.otherPercentValue_2.setFrameShape(QtWidgets.QFrame.Box)
        self.otherPercentValue_2.setText("")
        self.otherPercentValue_2.setObjectName("otherPercentValue_2")
        self.otherPercentage_2.addWidget(self.otherPercentValue_2)
        self.otherContainer_2.addLayout(self.otherPercentage_2)
        self.otherVBOX_2.addLayout(self.otherContainer_2)
        self.signCategories_2.addLayout(self.otherVBOX_2)
        self.FalseNegativeLabel = QtWidgets.QLabel(self.centralwidget)
        self.FalseNegativeLabel.setGeometry(QtCore.QRect(30, 170, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.FalseNegativeLabel.setFont(font)
        self.FalseNegativeLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.FalseNegativeLabel.setObjectName("FalseNegativeLabel")
        self.signCategoriesLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.signCategoriesLabel_2.setGeometry(QtCore.QRect(470, 150, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.signCategoriesLabel_2.setFont(font)
        self.signCategoriesLabel_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.signCategoriesLabel_2.setObjectName("signCategoriesLabel_2")
        FalseNegativeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FalseNegativeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName("menubar")
        FalseNegativeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FalseNegativeWindow)
        self.statusbar.setObjectName("statusbar")
        FalseNegativeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FalseNegativeWindow)
        QtCore.QMetaObject.connectSlotsByName(FalseNegativeWindow)

    def retranslateUi(self, FalseNegativeWindow):
        _translate = QtCore.QCoreApplication.translate
        FalseNegativeWindow.setWindowTitle(_translate("FalseNegativeWindow", "MainWindow"))
        self.titleLabel.setText(_translate("FalseNegativeWindow", "3D Point Cloud Autograder"))
        self.regulatoryLabel_2.setText(_translate("FalseNegativeWindow", "Regulatory:"))
        self.guidingLabel_2.setText(_translate("FalseNegativeWindow", "Guiding:"))
        self.warningLabel_2.setText(_translate("FalseNegativeWindow", "Warning:"))
        self.constructionLabel_2.setText(_translate("FalseNegativeWindow", "Construction:"))
        self.otherLabel_2.setText(_translate("FalseNegativeWindow", "Other:"))
        self.FalseNegativeLabel.setText(_translate("FalseNegativeWindow", "False Negative"))
        self.signCategoriesLabel_2.setText(_translate("FalseNegativeWindow", "Sign Categories:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FalseNegativeWindow = QtWidgets.QMainWindow()
    ui = Ui_FalseNegativeWindow()
    ui.setupUi(FalseNegativeWindow)
    FalseNegativeWindow.show()
    sys.exit(app.exec_())
