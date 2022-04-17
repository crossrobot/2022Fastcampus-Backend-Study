
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from Messenger import Ui_MainWindow 

from PySide6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow) : 
    def __init__(self) : 
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self) 
        self.myui.btn_send.clicked.connect(self.send)

        self.model = QStandardItemModel()
        self.myui.list_chatroom.setModel(self.model)



    def send(self) :
        text = self.myui.edit_chat.text()
        item = QStandardItem(text)
        # self.model은 QStandardItemModel의 객체이고, 이것은 QStandardItem 만 받을 수 있다. 
        # 따라서 model.appendRow() 안에 text를 집어 넣은 것이 아니라 item을 집어 넣은 것
        self.model.appendRow(item)


if __name__ == "__main__" : 
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
