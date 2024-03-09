import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QInputDialog,QMessageBox
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

import json

notes={
    "ласкаво просимо!":{
        "текст":"Привіт усім! Це моя крута програмка!",
        "теги" :["Привітання","старт"]
    },
    "Програмуваня!":{
        "текст":"Ми працюємо на мові Python",
        "теги":["Python","логіка"]
    }
}
with open("data.json","w",encoding="utf-8")as file:
    json.dump(notes,file,sort_keys=True)


class widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.list_notes.itemClicked.connect(self.show_note)
        self.ui.btn_kriet.clicked.connect(self.add_note)
        self.ui.btn_del_nout.clicked.connect(self.del_note)
        self.ui.btn_seyw_nout.clicked.connect(self.save_note)



    def show_note(self):
        key=self.ui.list_notes.selectedItems()[0].text()
        self.ui.text.setText(notes[key]["текст"])
        self.ui.list_tegs.clear()
        self.ui.list_tegs.addItems(notes[key]["теги"])

    def add_note(self):
        name,ok=QInputDialog.getText(self,"Додати замітку","Назва замітки")
        if ok==True and name !="":
            notes[name]={"Текст":"","теги":[]}
            self.ui.list_notes.addItem(name)

    def del_note(self):
        if self.ui.list_notes.selectedItems():
            key=self.ui.list_notes.selectedItems()[0].text()
            del notes[key]
            self.ui.list_notes.clear()
            self.ui.text.clear()
            self.ui.list_tegs.clear()
            self.ui.list_notes.addItems(notes)
            with open("data.json","w",encoding="utf-8")as file:
                json.dump(notes,file)

        else:
            win=QMessageBox()
            win.setText("Замітка для видаленя не вибрана")
            win.exec()



    def save_note(self):
        if self.ui.list_notes.selectedItems():
            key=self.ui.list_notes.selectedItems()[0].text()
            notes[key]["текст"]=self.ui.text.toPlainText()
            with open("data.json","w",encoding="utf-8")as file:
                json.dump(notes,file)

        else:
            win=QMessageBox()
            win.setText("Замітка для збереженя не вибрана")
            win.exec()


    def add_tag(self):
        if self.ui.list_notes.selectedItems():
         key=self.ui.list_notes.selectedItems()[0].text()
         tag=self.ui.lain_siarg.text()
        if tag not in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            self.ui.lain_siarg.clear()
            self.ui.list_tegs.addItem(tag)
            with open("data.json","w",encoding="utf-8")as file:
                json.dump(notes,file)

        else:
            win=QMessageBox()
            win.setText("Замітка для доданя тегу не вибрана")
            win.exec()
    def del_tag(self):
        if self.ui.list_notes.selectedItems():
            key=self.ui.list_notes.selectedItems()[0].text()
            tag=self.ui.list_tegs.selectedItems()[0].text()
            notes[key]["теги"].remove(tag)
            self.ui.list_tegs.clear()
            self.ui.list_tegs.addItems(notes[key]["теги"])
            with open("data.json","w",encoding="utf-8")as file:
                json.dump(notes,file)

        else:
            win=QMessageBox()
            win.setText("Замітка для видаленя  тегу не вибрана")
            win.exec()

    def search_tag(self):
        if self.ui.lain_siarg.text()!="":
            if self.ui.btn_seyw_nout.text()=="Шукати замітки по тегу":
                notes_filtes={}
                tag=self.ui.lain_siarg.text()
                for note in notes:
                    notes_filtes[note]=notes[note]
                self.ui.list_notes.clear()
                self.ui.list_tegs.clear()
                self.ui.text.clear()
                self.ui.list_notes.addItems(notes_filtes)




app=QApplication([])
ex=widget()
ex.show()

with open("data.json","r",encoding="utf-8")as file:
    notes=json.load(file)
    ex.ui.list_notes.addItems(notes)

app.exec_()
