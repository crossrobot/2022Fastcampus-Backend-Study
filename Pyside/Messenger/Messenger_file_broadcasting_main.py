from re import L
import sys 

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from Messenger_listwidget버전 import Ui_MainWindow
import random
from PySide6.QtCore import QTimer

class MainWindow(QMainWindow) : 
    last_read = 0

    def __init__(self) : 
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_send.clicked.connect(self.send)
        ## 채팅창에서 엔터를 누를 때 전송되는 기능  
        self.ui.edit_chat.returnPressed.connect(self.send)

        # 아래에 있는 랜덤 닉네임 생성함수를 갖고 온다
        nickname = self.random_nickname()
        self.ui.edit_nickname.setText(nickname)

        # 환영합니다 메시지 
        with open(r"C:\Users\USER\임낙준_패캠백엔드\Pyside\Messenger\server.txt", "a+",  encoding = 'utf-8') as f : 
            f.writelines(f'-----------{nickname}님이 입장하셨습니다.----------------')

        

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.listen)
        
        self.timer.start()

## listWidget 으로 구현할 경우
## listview와 달리 model이 그 자체에 내장되어 있어 보다 간결한 코딩이 가능하다

    # 메신저 보내기 : 버튼 클릭이나 엔터 누르면 실행됌 
    def send(self) : 
        nickname = self.ui.edit_nickname.text()
        text = self.ui.edit_chat.text()
        msg = f"{nickname}: {text}"

        # 파일에다가 msg를 쓰는 것 
        with open(r"C:\Users\USER\임낙준_패캠백엔드\Pyside\Messenger\server.txt",'a+',encoding = 'utf-8') as f : 
            f.writelines(msg+ "\n")

        self.ui.edit_chat.clear()
        #self.ui.edit_nickname.clear()

        # 읽어오기 
        # self.listen()       주석처리. 이 역할을 위의 QTimer에서 실행되도록 함. 

    #  임의로 닉네임을 생성해 주는 함수 
    def random_nickname(self) : 
        nickname = random.choice(["홍길동","박보검","한소희"])
        num = random.randint(1,1000)
        return f"{nickname}{num}"


    def listen(self) : 
        try : 
            with open(r"C:\Users\USER\임낙준_패캠백엔드\Pyside\Messenger\server.txt", "r", encoding = "utf-8") as f:
                lines = f.readlines()
            
            lines = [x.strip() for x in lines]
            self.ui.list_chatroom.addItems(lines[self.last_read : ])
            self.last_read = len(lines) 
            self.ui.list_chat.scrollToBottom() # listen 할 때마다 스크롤을 하도록. 
        except : 
            pass


if __name__ == "__main__" : 
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())