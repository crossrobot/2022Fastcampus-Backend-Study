import sys 

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from Messenger_listwidget버전 import Ui_MainWindow
import random


class MainWindow(QMainWindow) : 
    def __init__(self) : 
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_send.clicked.connect(self.click)
        ## 채팅창에서 엔터를 누를 때 전송되는 기능  
        self.ui.edit_chat.returnPressed.connect(self.click)

        # 아래에 있는 랜덤 닉네임 생성함수를 갖고 온다
        nickname = self.random_nickname()
        self.ui.edit_nickname.setText(nickname)

## listWidget 으로 구현할 경우
## listview와 달리 model이 그 자체에 내장되어 있어 보다 간결한 코딩이 가능하다

    def click(self) : 
        nickname = self.ui.edit_nickname.text()
        text = self.ui.edit_chat.text()
        msg = f"{nickname}: {text}"

        # 파일에다가 msg를 쓰는 것 
        with open('./server.txt','a+',encoding = 'utf-8') as f : 
            f.writelines(msg)

        self.ui.edit_chat.clear()
        self.ui.edit_nickname.clear()

    #  임의로 닉네임을 생성해 주는 함수 
    def random_nickname(self) : 
        nickname = random.choice(["홍길동","박보검","한소희"])
        num = random.randint(1,1000)
        return f"{nickname}{num}"

if __name__ == "__main__" : 
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())