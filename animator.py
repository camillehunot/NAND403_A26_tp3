import os
import random
import sys

from maya import cmds
from PySide6.QtWidgets import ( QMessageBox, )

import importlib
import ui
importlib.reload(ui)

class RandomAnimation:
    def __init__(self):
        self.ui = ui.RandomAnimationUI()
        self.ui.button.clicked.connect(self.on_click)
        #en gros : quand on clic sur le bouton (du ui), on appelle la fonction random_value


    def check_selection(self):
    
    
            item_selected= cmds.ls(selection=True) #permet de récupérer les objets selectionnés dans maya et de les mettre dans la variable item_selected
        
            if not item_selected: #si aucun item n'est selectionné, on affiche un message d'erreur
                QMessageBox.warning(self.ui, "Warning", "Nothing selected in the outliner")

                return None
            return item_selected

    
    def random_value(self): 
        #on récupère les valeur et on les met directement dans un random pour obtenir notre valeur aléatoire
    
        value_duration = self.ui.timing_duration.value()
        value_step = self.ui.timing_step.value()
    
        random_translate_x = self.ui.translate_spin_min_x.value()
        random_translate_y = self.ui.translate_spin_min_y.value()
        random_translate_z = self.ui.translate_spin_min_z.value()
    
        random_rotate_x = self.ui.rotate_spin_min_x.value()
        random_rotate_y = self.ui.rotate_spin_min_y.value()
        random_rotate_z = self.ui.rotate_spin_min_z.value()
    
        random_scale_x = self.ui.scale_spin_min_x.value()
        random_scale_y = self.ui.scale_spin_min_y.value()
        random_scale_z = self.ui.scale_spin_min_z.value()


    def on_click(self):
        self.ui.random_value()
        self.check_selection()
        self.random_value()


    

    