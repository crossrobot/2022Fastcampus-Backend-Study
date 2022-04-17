import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from Greetingprogram2 import Ui_MainWindow

class MainWindow(QMainWindow) : 
    def __init__(self) : 
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_hi.clicked.connect(self.click)   ### self.click()이 아니라 self.click씀으로써 함수를 '호출'하지 않고 바로 넣었다. 
        # click이라는 시그널이 발생될 때마다 click이라는 함수가 실행되어야 하기 때문




    def click(self) : 
       self.ui.btn_hi.setText("메롱")

       self.ui.checkBox.setChecked(True)
       self.ui.checkBox_3.setChecked(True)
       self.ui.checkBox_2.setChecked(True)

       if self.ui.radioButton.isChecked() : 
           self.ui.radioButton_2.setChecked(True) 

       elif self.ui.radioButton_2.isChecked() : 
           self.ui.radioButton.setChecked(True) 

       else : 
           self.ui.radioButton.setChecked(True)



if __name__ == "__main__" : 
    app = QApplication()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())