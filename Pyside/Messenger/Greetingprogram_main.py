import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from Greetingprogram import Ui_MainWindow

class MainWindow(QMainWindow) : 
    def __init__(self) : 
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_hi.clicked.connect(self.click)   ### self.click()이 아니라 self.click씀으로써 함수를 '호출'하지 않고 바로 넣었다. 
        # click이라는 시그널이 발생될 때마다 click이라는 함수가 실행되어야 하기 때문

        self.ui.btn_hi.clicked 


    def click(self) : 
       mb_hi = QMessageBox()
       mb_hi.setText("안녕하세요")
       mb_hi.exec()

       mb_quiz = QMessageBox()
       mb_quiz.setText("1+1?")

       ##  Qmessgebox의 Role들은 여러가지가 있다.
       ##  그 Role 들의 가장 큰 특징은, default 위치가 다른것. 
       ## 자세한 내용은 Qt 홈페이지 상에서 role의 상세설명을 봐라. 

       btn_answer_2 = mb_quiz.addButton("2", QMessageBox.ActionRole)
       btn_answer_3 = mb_quiz.addButton("3", QMessageBox.ActionRole)
       res = mb_quiz.exec() 
       print(res)

       if mb_quiz.clickedButton() == btn_answer_2:
           print("정답!")
           mb_success = QMessageBox()
           mb_success.setText("정답입니다!!")
           mb_success.exec()
    
       elif mb_quiz.clickedButton() == btn_answer_3 : 
            print("wrong")
            print("정답!")
            mb_success = QMessageBox()
            mb_success.setText("오답입니다ㅠㅠ")
            mb_success.exec()


if __name__ == "__main__" : 
    app = QApplication()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())