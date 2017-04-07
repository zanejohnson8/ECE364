import sys

from PySide.QtGui import *
from BasicUI import *
import re


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.txt = [self.txtStudentName, self.txtStudentID, self.txtComponentName_1, self.txtComponentCount_1 , self.txtComponentName_2, self.txtComponentCount_2 , self.txtComponentName_3, self.txtComponentCount_3 , self.txtComponentName_4, self.txtComponentCount_4 , self.txtComponentName_5, self.txtComponentCount_5 , self.txtComponentName_6, self.txtComponentCount_6 , self.txtComponentName_7, self.txtComponentCount_7 , self.txtComponentName_8, self.txtComponentCount_8 , self.txtComponentName_9, self.txtComponentCount_9 , self.txtComponentName_10, self.txtComponentCount_10 , self.txtComponentName_11, self.txtComponentCount_11 , self.txtComponentName_12, self.txtComponentCount_12 , self.txtComponentName_13, self.txtComponentCount_13 , self.txtComponentName_14, self.txtComponentCount_14 , self.txtComponentName_15, self.txtComponentCount_15 , self.txtComponentName_16, self.txtComponentCount_16 , self.txtComponentName_17, self.txtComponentCount_17 , self.txtComponentName_18, self.txtComponentCount_18 , self.txtComponentName_19, self.txtComponentCount_19 , self.txtComponentName_20, self.txtComponentCount_20]
        self.buttons = [self.btnClear, self.btnLoad, self.btnSave]
        self.btnClear.clicked.connect(self.clear)

        self.btnSave.clicked.connect(self.save)
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(True)
        self.btnLoad.clicked.connect(self.loadData)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        with open(filePath, "r") as signalFile:
            lines = signalFile.readlines()
        templine = lines[2]
        expr = r"\"(?P<grad>[truefals]{4,5})\""
        match = re.search(expr, templine, re.I)
        if (match):
            grad = match.group("grad")
            if (grad == 'true'):
                self.chkGraduate.setChecked(True)
            else:
                self.chkGraduate.setChecked(False)

        templine = lines[2]
        expr = r">(?P<grad>[\w\s]+)<"
        match = re.search(expr, templine, re.I)
        if (match):
            grad = match.group("grad")
            self.txtStudentName.setText(grad)

        templine = lines[3]
        expr = r">(?P<grad>[0-9-]+)<"
        match = re.search(expr, templine, re.I)
        if (match):
            grad = match.group("grad")
            self.txtStudentID.setText(grad)

        templine = lines[4]
        expr = r">(?P<grad>[\w\s]+)<"
        match = re.search(expr, templine, re.I)
        if (match):
            grad = match.group("grad")
            if (grad == 'Industrial Engineering'):
                self.cboCollege.setCurrentIndex(5)
            if (grad == 'Aerospace Engineering'):
                self.cboCollege.setCurrentIndex(1)
            if (grad == 'Civil Engineering'):
                self.cboCollege.setCurrentIndex(2)
            if (grad == 'Computer Engineering'):
                self.cboCollege.setCurrentIndex(3)
            if (grad == 'Electrical Engineering'):
                self.cboCollege.setCurrentIndex(4)
            if (grad == 'Mechinical Engineering'):
                self.cboCollege.setCurrentIndex(6)

        i = 5
        k = 0
        while i < len(lines) - 2:
            templine = lines[i]
            expr1 = r"name=\"(?P<name>[\w\d\s-]+)\""
            match1 = re.search(expr1, templine, re.I)
            expr2 = r"count=\"(?P<count>[\w\d\s-]+)\""
            match2 = re.search(expr2, templine, re.I)
            if (match1 and match2):
                name = match1.group("name")
                count = match2.group("count")
                self.txt[k].setText(name)
                self.txt[k + 1].setText(count)
            k += 2
            i += 1






    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def clear(self):
        self.cboCollege.setCurrentIndex(0)
        self.chkGraduate.setChecked(False)
        for box in self.txt:
            box.setText('')


    def save(self):
        s = str()
        s += '<?xml version="1.0" encoding="UTF-8"?>\n<Content>\n\t<StudentName graduate="'
        if (self.chkGraduate.isChecked()):
            s += 'true'
        else:
            s += 'false'
        s += '">'
        s += self.txtStudentName.text()
        s += '</StudentName>\n\t'
        s += '<StudentID>'
        s += self.txtStudentID.text()
        s += '</StudentID>\n\t'
        s += '<College>'
        s += self.cboCollege.currentText()
        s += '</College>\n\t<Components>\n'
        i = 2
        while i < len(self.txt):
            curbox = self.txt[i]
            curboxn = self.txt[i + 1]
            if len(curbox.text()) != 0:
                s += '\t\t<Component name="'
                s += curbox.text()
                s += '" count="'
                s += curboxn.text()
                s += '" />\n'
            i += 2
        s += '\t</Components>\n</Content>'
        f = open('target.xml', 'w')
        f.write(s)



    def saveEnable(self):
        cnt = 0
        for box in self.txt:
            if len(box.text()) == 0:
                cnt += 0
            else:
                cnt += 1
        print(cnt)
        if (cnt > 0):

            self.btnSave.setEnabled(True)
            self.btnLoad.setEnabled(False)

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
