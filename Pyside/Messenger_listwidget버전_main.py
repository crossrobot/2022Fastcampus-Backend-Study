import sys 

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from Messenger_listwidget버전 import Ui_MainWindow


class MainWindow(QMainWindow) : 
    def __init__(self) :  
        super().__init__() 
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self) 
        self.ui.btn_send.clicked.connect(self.click)

        ## 채팅창에서 엔터를 누를 때 전송되는 기능  
        self.ui.edit_chat.returnPressed.connect(self.click)

        ## 

## listWidget 으로 구현할 경우
## listview와 달리 model이 그 자체에 내장되어 있어 보다 간결한 코딩이 가능하다

    def click(self) : 
        text = self.ui.edit_chat.text()
        nickname = self.ui.edit_nickname.text()
        self.ui.list_chatroom.addItem(f"{nickname} : {text}")
        self.ui.edit_chat.clear()
        self.ui.edit_nickname.clear()

if __name__ == "__main__" : 
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())