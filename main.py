import sys
from PyQt5 import QtGui, QtWidgets
from base_ui import Ui_MainWindow
import mysql.connector
from mysql.connector import errorcode
from functools import cmp_to_key
import numpy as np


def compare_func(t1,t2):
    return t1[1] - t2[1]

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.setWindowTitle("WINDOW TITLE")

        self.alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.ui.gb1_comboBox_A.addItems(self.alpha)
        self.ui.gb1_comboBox_B.addItems(self.alpha)
        self.ui.gb1_comboBox_C.addItems(self.alpha)
        self.ui.gb2_comboBox_A.addItems(self.alpha)
        self.ui.gb2_comboBox_B.addItems(self.alpha)
        self.ui.gb2_comboBox_C.addItems(self.alpha)
        self.ui.gb3_comboBox_A.addItems(self.alpha)
        self.ui.gb3_comboBox_B.addItems(self.alpha)
        self.ui.gb3_comboBox_C.addItems(self.alpha)
        self.ui.gb4_comboBox_A.addItems(self.alpha)
        self.ui.gb4_comboBox_B.addItems(self.alpha)
        self.ui.gb4_comboBox_C.addItems(self.alpha)

        self.ui.gb1_comboBox_A.setCurrentIndex(0)
        self.ui.gb1_comboBox_B.setCurrentIndex(1)
        self.ui.gb1_comboBox_C.setCurrentIndex(2)
        self.ui.gb2_comboBox_A.setCurrentIndex(3)
        self.ui.gb2_comboBox_B.setCurrentIndex(4)
        self.ui.gb2_comboBox_C.setCurrentIndex(5)
        self.ui.gb3_comboBox_A.setCurrentIndex(6)
        self.ui.gb3_comboBox_B.setCurrentIndex(7)
        self.ui.gb3_comboBox_C.setCurrentIndex(8)
        self.ui.gb4_comboBox_A.setCurrentIndex(9)
        self.ui.gb4_comboBox_B.setCurrentIndex(10)
        self.ui.gb4_comboBox_C.setCurrentIndex(11)

        self.ui.generate_pb.clicked.connect(self.generate)
        self.ui.wl_listWidget.doubleClicked.connect(self.add_list_word)
        self.ui.solution_rmv_pb.clicked.connect(self.rmv_sol_word)
        self.ui.solution_add_pb.clicked.connect(self.add_word)

        self.cnx = self.mysql_initialize(self)

        if self.cnx is None:
            sys.exit()

        self.fstr = ""
        self.word_list = None
        self.words = []
        self.groups = []
        self.uc_letters = ""

    def generate(self):
        if self.words:
            self.words.clear()
            self.update_letterbox_color()

        self.ui.wl_listWidget.clear()
        self.groups.clear()

        self.groups.append(self.alpha[self.ui.gb1_comboBox_A.currentIndex()]
                           + self.alpha[self.ui.gb1_comboBox_B.currentIndex()]
                           + self.alpha[self.ui.gb1_comboBox_C.currentIndex()])
        self.groups.append(self.alpha[self.ui.gb2_comboBox_A.currentIndex()]
                           + self.alpha[self.ui.gb2_comboBox_B.currentIndex()]
                           + self.alpha[self.ui.gb2_comboBox_C.currentIndex()])
        self.groups.append(self.alpha[self.ui.gb3_comboBox_A.currentIndex()]
                           + self.alpha[self.ui.gb3_comboBox_B.currentIndex()]
                           + self.alpha[self.ui.gb3_comboBox_C.currentIndex()])
        self.groups.append(self.alpha[self.ui.gb4_comboBox_A.currentIndex()]
                           + self.alpha[self.ui.gb4_comboBox_B.currentIndex()]
                           + self.alpha[self.ui.gb4_comboBox_C.currentIndex()])

        self.fstr =  "".join(self.groups)

        ex_str = ""
        for c in self.alpha:
            if c in self.fstr:
                continue
            ex_str += c

        print(ex_str)
        data = self.mysql_query(ex_str)
        data = self.process_data(data)
        data.sort(key=len)
        data.reverse()
        self.uc_letters = self.fstr

        ol = [ (s , self.unchecked_letters_count(s.upper())) for s in data]
        ol.sort(key=cmp_to_key(compare_func))
        ol.reverse()
        self.word_list = [x[0] for x in ol]
        self.ui.wl_listWidget.addItems(self.word_list)
        self.ui.solution_label.setText("Solution: ")

    def process_data(self, data):
        out =  set()
        for d in data:

            if "_" in d:
                for x in d.split("_"):
                    if self.check_str_against_fstr(x.upper()):
                        out.add(x)
            else:
                if self.check_str_against_fstr(d.upper()):
                    out.add(d)

        ol = []
        for x in out:
            if self.check_str_against_groups(x.upper()) and len(x) >= 3:
                ol.append(x)
        return ol

    def check_str_against_fstr(self, str):
        flg = True
        for c in str:
            if not(c in self.fstr):
                flg = False
                break

        return flg

    def check_str_against_groups(self, str ):
        flg = True
        gp = self.get_group(str[0])
        for c in str[1:]:
            g = self.get_group(c)
            if g == gp:
                flg = False
                break
            gp = g
        return flg

    def get_group(self, c):
        for i in range(len(self.groups)):
            if c in self.groups[i]:
                return i
        return None

    def add_list_word(self):
        word = self.ui.wl_listWidget.currentItem().text().upper()
        self.words.append(word)
        self.ui.solution_label.setText( "Solution: " + self.build_sol_str(self.words))
        self.update_letterbox_color()
        tmp = []
        for w in self.word_list:
            wu = w.upper()
            if word[-1] == wu[0]:
                tmp.append(w)

        ol = [(s, self.unchecked_letters_count(s.upper())) for s in tmp]
        ol.sort(key=cmp_to_key(compare_func))
        ol.reverse()
        self.ui.wl_listWidget.clear()
        self.ui.wl_listWidget.addItems([x[0] for x in ol])
        print(ol)

    def add_word(self):
        word = self.ui.solution_add_lineEdit.text().upper()
        print(word)
        if word:
            self.words.append(word)
            self.ui.solution_label.setText("Solution: " + self.build_sol_str(self.words))
            self.update_letterbox_color()
            tmp = []
            for w in self.word_list:
                wu = w.upper()
                if word[-1] == wu[0]:
                    tmp.append(w)

            ol = [(s, self.unchecked_letters_count(s.upper())) for s in tmp]
            ol.sort(key=cmp_to_key(compare_func))
            ol.reverse()
            self.ui.wl_listWidget.clear()
            self.ui.wl_listWidget.addItems([x[0] for x in ol])


    def rmv_sol_word(self):
        if not self.words:
            return
        self.ui.wl_listWidget.clear()
        self.words.pop(-1)
        self.update_letterbox_color()
        if self.words:
            word = self.words[-1]
            tmp = []
            for w in self.word_list:
                wu = w.upper()
                if word[-1] == wu[0]:
                    tmp.append(w)

            ol = [(s, self.unchecked_letters_count(s.upper())) for s in tmp]
            ol.sort(key=cmp_to_key(compare_func))
            ol.reverse()
            self.ui.wl_listWidget.addItems([x[0] for x in ol])
        else:
            self.ui.wl_listWidget.addItems(self.word_list)
        self.ui.solution_label.setText("Solution: " + self.build_sol_str(self.words))

        print(self.uc_letters)

    def unchecked_letters_count(self, str):
        checked = ""
        cnt = 0
        for a in str:
            if (a in self.uc_letters) and not(a in checked):
                cnt += 1
            checked += a

        return cnt

    def build_sol_str(self, wrds):
        str = ""
        if wrds:
            str += wrds[0].upper()
        for w in  wrds[1:]:
            str += "-" + w.upper()
        return str

    def update_letterbox_color(self):
        str = self.build_sol_str(self.words)
        self.uc_letters = ""

        palg = self.ui.gb1_comboBox_A.palette()
        palw = self.ui.gb1_comboBox_B.palette()
        palg.setColor(QtGui.QPalette.Button, QtGui.QColor(0, 255, 0))
        palw.setColor(QtGui.QPalette.Button, QtGui.QColor(255, 255, 255))

        # GROUP1
        if self.alpha[self.ui.gb1_comboBox_A.currentIndex()] in str:
            self.ui.gb1_comboBox_A.setPalette(palg)
        else:
            self.ui.gb1_comboBox_A.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb1_comboBox_A.currentIndex()]

        if self.alpha[self.ui.gb1_comboBox_B.currentIndex()] in str:
            self.ui.gb1_comboBox_B.setPalette(palg)
        else:
            self.ui.gb1_comboBox_B.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb1_comboBox_B.currentIndex()]

        if self.alpha[self.ui.gb1_comboBox_C.currentIndex()] in str:
            self.ui.gb1_comboBox_C.setPalette(palg)
        else:
            self.ui.gb1_comboBox_C.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb1_comboBox_C.currentIndex()]

        # GROUP2
        if self.alpha[self.ui.gb2_comboBox_A.currentIndex()] in str:
            self.ui.gb2_comboBox_A.setPalette(palg)
        else:
            self.ui.gb2_comboBox_A.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb2_comboBox_A.currentIndex()]

        if self.alpha[self.ui.gb2_comboBox_B.currentIndex()] in str:
            self.ui.gb2_comboBox_B.setPalette(palg)
        else:
            self.ui.gb2_comboBox_B.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb2_comboBox_B.currentIndex()]

        if self.alpha[self.ui.gb2_comboBox_C.currentIndex()] in str:
            self.ui.gb2_comboBox_C.setPalette(palg)
        else:
            self.ui.gb2_comboBox_C.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb2_comboBox_C.currentIndex()]

        # GROUP3
        if self.alpha[self.ui.gb3_comboBox_A.currentIndex()] in str:
            self.ui.gb3_comboBox_A.setPalette(palg)
        else:
            self.ui.gb3_comboBox_A.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb3_comboBox_A.currentIndex()]

        if self.alpha[self.ui.gb3_comboBox_B.currentIndex()] in str:
            self.ui.gb3_comboBox_B.setPalette(palg)
        else:
            self.ui.gb3_comboBox_B.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb3_comboBox_B.currentIndex()]

        if self.alpha[self.ui.gb3_comboBox_C.currentIndex()] in str:
            self.ui.gb3_comboBox_C.setPalette(palg)
        else:
            self.ui.gb3_comboBox_C.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb3_comboBox_C.currentIndex()]

        # GROUP4
        if self.alpha[self.ui.gb4_comboBox_A.currentIndex()] in str:
            self.ui.gb4_comboBox_A.setPalette(palg)
        else:
            self.ui.gb4_comboBox_A.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb4_comboBox_A.currentIndex()]

        if self.alpha[self.ui.gb4_comboBox_B.currentIndex()] in str:
            self.ui.gb4_comboBox_B.setPalette(palg)
        else:
            self.ui.gb4_comboBox_B.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb4_comboBox_B.currentIndex()]

        if self.alpha[self.ui.gb4_comboBox_C.currentIndex()] in str:
            self.ui.gb4_comboBox_C.setPalette(palg)
        else:
            self.ui.gb4_comboBox_C.setPalette(palw)
            self.uc_letters += self.alpha[self.ui.gb4_comboBox_C.currentIndex()]

    @staticmethod
    def mysql_initialize(self):
        try:
            cx = mysql.connector.connect(user='lebrown', password='mydbPass1990',
                                         host='localhost',
                                         database='wn_pro_mysql')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                return None
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return None
            else:
                print(err)
                return None

        print("Connection successful!!")
        return cx

    def mysql_query(self, str):
        q = "SELECT word FROM `wn_synset` WHERE upper(word) NOT LIKE '%{}%'".format(str[0])

        for c in str[1:]:
            q += " AND upper(word) NOT LIKE '%{}%'".format(c)

        cursor = self.cnx.cursor()
        cursor.execute(q)

        print(cursor)

        rsp =[]
        for row in cursor:
            rsp.append(row[0])
        cursor.close()
        return rsp





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())