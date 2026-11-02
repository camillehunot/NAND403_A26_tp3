import os
import sys
from maya import cmds
from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout,QTextEdit, QPushButton, QMessageBox, QApplication, QCheckBox, QLineEdit)

import importlib
import animator
importlib.reload(animator)


class RandomAnimationUI(QWidget):
    def __init__(self): #constructeur self équivalent de this du cpp, le constructeur dans python prend self en paramètre
        super().__init__() # Constructeur de notre parent (super = mot clé générique pour l'héritage)
        self.setWindowTitle("Random Animation Tool")   #fonction qui existe déjà dans QWidget self(en gros la class messageBoard) appel la fonction setWindoTitle
        self.create_ui()#pas besoin de mettre self ici. permet d'appeler notre fonction create UI

    def create_ui(self):

        app = QApplication.instance() #permet de récupérer l'instance de l'application, toujours avant un QWidget 
        layout = QVBoxLayout(self)   #container
        title = QLabel("message board")
        layout.addWidget(title)