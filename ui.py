import os
import random
import sys
from maya import cmds
from PySide6.QtWidgets import (QHBoxLayout, QWidget, QSpinBox,QGroupBox, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QMessageBox, QApplication, QCheckBox, QLineEdit)

import importlib
import animator
importlib.reload(animator)


class RandomAnimationUI(QWidget):
    def __init__(self): #constructeur self équivalent de this du cpp, le constructeur dans python prend self en paramètre
        super().__init__() # Constructeur de notre parent (super = mot clé générique pour l'héritage)
        self.setWindowTitle("Random Animation Tool")  
        self.create_ui()#pas besoin de mettre self ici. permet d'appeler notre fonction create UI

    def create_ui(self):

        app = QApplication.instance() #permet de récupérer l'instance de l'application, toujours avant un QWidget 
        layout = QVBoxLayout(self)   #container
        

        ##############################################################################################
        ########################## Création des champs de paramètres #################################
        ##############################################################################################

        timing_grp, timing_internal_layout = self.create_group_box("Timing") 
        translate_grp, translate_internal_layout = self.create_group_box("Translate")
        rotate_grp, rotate_internal_layout = self.create_group_box("Rotate")
        scale_grp, scale_internal_layout = self.create_group_box("Scale")

        layout.addWidget(timing_grp)
        layout.addWidget(translate_grp)
        layout.addWidget(rotate_grp)
        layout.addWidget(scale_grp)

        #################################################

        timing_duration_layout = self.create_Horizontal_layout()
        timing_step_layout = self.create_Horizontal_layout()

        translate_min_layout = self.create_Horizontal_layout()
        translate_max_layout = self.create_Horizontal_layout()

        rotate_min_layout = self.create_Horizontal_layout()
        rotate_max_layout = self.create_Horizontal_layout()

        scale_min_layout = self.create_Horizontal_layout()
        scale_max_layout = self.create_Horizontal_layout()


        #################################################

        timing_internal_layout.addLayout(timing_duration_layout)
        timing_internal_layout.addLayout(timing_step_layout) 

        translate_internal_layout.addLayout(translate_min_layout)
        translate_internal_layout.addLayout(translate_max_layout)   

        rotate_internal_layout.addLayout(rotate_min_layout)
        rotate_internal_layout.addLayout(rotate_max_layout)         

        scale_internal_layout.addLayout(scale_min_layout)
        scale_internal_layout.addLayout(scale_max_layout)   

        #################################################
        # Comme la fonction create_spin_box retourne un layout et un spinbox, 
        # on peut récupérer les deux valeurs dans deux variables différentes et ca place la seconde

        timing_duration, self.timing_duration = self.create_spin_box("Durations (Frames) :", 1, 1000, 100)
        timing_step, self.timing_step = self.create_spin_box("Step (Frames) :", 1, 100, 30)

        translate_min_x, self.translate_spin_min_x = self.create_spin_box("min x :", -100, 100, 10)   
        translate_min_y, self.translate_spin_min_y = self.create_spin_box("min y :", -100, 100, 10) 
        translate_min_z, self.translate_spin_min_z = self.create_spin_box("min z :", -100, 100, 10)

        translate_max_x, self.translate_spin_max_x = self.create_spin_box("max x :",-100,    100, 10) 
        translate_max_y, self.translate_spin_max_y = self.create_spin_box("max y :", -100, 100, 10)
        translate_max_z, self.translate_spin_max_z = self.create_spin_box("max z :", -100, 100, 10)

        rotate_min_x, self.rotate_spin_min_x = self.create_spin_box("min x :", -360, 360, 10)
        rotate_min_y, self.rotate_spin_min_y = self.create_spin_box("min y :", -360, 360, 10)
        rotate_min_z, self.rotate_spin_min_z = self.create_spin_box("min z :", -360,  360, 10)        

        rotate_max_x, self.rotate_spin_max_x = self.create_spin_box("max x :", -360, 100, 10)
        rotate_max_y, self.rotate_spin_max_y = self.create_spin_box("max y :", -360, 100, 10)
        rotate_max_z, self.rotate_spin_max_z = self.create_spin_box("max z :", -360, 100, 10)

        scale_min_x, self.scale_spin_min_x = self.create_spin_box("min x :", 1, 100, 10)
        scale_min_y, self.scale_spin_min_y = self.create_spin_box("min y :", 1, 100, 10)
        scale_min_z, self.scale_spin_min_z = self.create_spin_box("min z :", 1, 100, 10)

        scale_max_x, self.scale_spin_max_x = self.create_spin_box("max x :", 1, 100, 10)
        scale_max_y, self.scale_spin_max_y = self.create_spin_box("max y :", 1, 100, 10)
        scale_max_z, self.scale_spin_max_z = self.create_spin_box("max z :", 1, 100, 10)   

        #################################################
        # On place les layout (contenant les spinbox) dans les layout des groupbox

        timing_duration_layout.addLayout(timing_duration)
        timing_step_layout.addLayout(timing_step)

        translate_min_layout.addLayout(translate_min_x)
        translate_min_layout.addLayout(translate_min_y)
        translate_min_layout.addLayout(translate_min_z)
        translate_max_layout.addLayout(translate_max_x)
        translate_max_layout.addLayout(translate_max_y)
        translate_max_layout.addLayout(translate_max_z)

        rotate_min_layout.addLayout(rotate_min_x)
        rotate_min_layout.addLayout(rotate_min_y)   
        rotate_min_layout.addLayout(rotate_min_z)
        rotate_max_layout.addLayout(rotate_max_x)
        rotate_max_layout.addLayout(rotate_max_y)
        rotate_max_layout.addLayout(rotate_max_z)

        scale_min_layout.addLayout(scale_min_x)
        scale_min_layout.addLayout(scale_min_y)
        scale_min_layout.addLayout(scale_min_z)
        scale_max_layout.addLayout(scale_max_x)
        scale_max_layout.addLayout(scale_max_y)
        scale_max_layout.addLayout(scale_max_z)     

        ##############################################################################################
        ###################### Création des champs de paramètres terminés ############################
        ##############################################################################################



        # Création du bouton et sa connexion à  on_click 
        self.button = QPushButton("generate", self) #ajouter un string pour ajouter du texte sur notre bouton
        layout.addWidget(self.button)
        #  self.button.clicked.connect(self.random_value) 






    def create_group_box(self, title):
        group_box = QGroupBox(title)
        layout = QVBoxLayout()
        group_box.setLayout(layout)
        return group_box, layout

    def create_Horizontal_layout(self):
        layout = QHBoxLayout()
        return layout   

    def create_spin_box(self, label_text, min_value, max_value, default_value):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        spin_box = QSpinBox()
        spin_box.setRange(min_value, max_value)
        spin_box.setValue(default_value)

        layout.addWidget(label)
        layout.addWidget(spin_box)
        
        return layout, spin_box  #attention ca retounre un layout et ensuite un spinbox, donc il faut faire attention à comment on va l'utiliser.


    def random_value(self): 

        
       #on récupère les valeur et on les met directement dans un random pour obtenir notre valeur aléatoire

        self.value_duration = self.timing_duration.value()
        self.value_step = self.timing_step.value()

        self.random_translate_x = random.uniform(self.translate_spin_min_x.value(), self.translate_spin_max_x.value())
        self.random_translate_y = random.uniform(self.translate_spin_min_y.value(), self.translate_spin_max_y.value())
        self.random_translate_z = random.uniform(self.translate_spin_min_z.value(), self.translate_spin_max_z.value())

        self.random_rotate_x = random.uniform(self.rotate_spin_min_x.value(), self.rotate_spin_max_x.value())
        self.random_rotate_y = random.uniform(self.rotate_spin_min_y.value(), self.rotate_spin_max_y.value())
        self.random_rotate_z = random.uniform(self.rotate_spin_min_z.value(), self.rotate_spin_max_z.value())

        self.random_scale_x = random.uniform(self.scale_spin_min_x.value(), self.scale_spin_max_x.value())
        self.random_scale_y = random.uniform(self.scale_spin_min_y.value(), self.scale_spin_max_y.value())
        self.random_scale_z = random.uniform(self.scale_spin_min_z.value(), self.scale_spin_max_z.value())

        return self.value_duration, self.value_step, self.random_translate_x, self.random_translate_y, self.random_translate_z, self.random_rotate_x, self.random_rotate_y, self.random_rotate_z, self.random_scale_x, self.random_scale_y, self.random_scale_z



    #def on_click(self): 

        