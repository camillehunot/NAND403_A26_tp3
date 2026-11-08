import os
import random
import sys
import ui

import importlib
import ui
importlib.reload(ui).RandomAnimationUI

class RandomAnimation:
    def __init__(self):
        self.ui = ui.RandomAnimationUI()
        self.ui.button.clicked.connect(self.random_value)
        #en gros : quand on clic sur le bouton (du ui), on appelle la fonction random_value

    
    def random_value(self): 
    
            
           #on récupère les valeur et on les met directement dans un random pour obtenir notre valeur aléatoire
    
            value_duration = self.ui.duration.value()
            value_step = self.ui.step.value()
    
            random_translate_x = self.ui.translate_x.value()
            random_translate_y = self.ui.translate_y.value()
            random_translate_z = self.ui.translate_z.value()
    
            rotate_translate_x = self.ui.rotate_x.value()
            rotate_translate_y = self.ui.rotate_y.value()
            rotate_translate_z = self.ui.rotate_z.value()
    
            scale_translate_x = self.ui.scale_translate_x.value()
            scale_translate_y = self.ui.scale_translate_y.value()
            scale_translate_z = self.ui.scale_translate_z.value()

    