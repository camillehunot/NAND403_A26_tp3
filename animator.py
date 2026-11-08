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
        self.ui.show()


    def check_selection(self):
    
    
            item_selected= cmds.ls(selection=True) #permet de récupérer les objets selectionnés dans maya et de les mettre dans la variable item_selected
        
            if not item_selected: #si aucun item n'est selectionné, on affiche un message d'erreur
                QMessageBox.warning(self.ui, "Warning", "Nothing selected in the outliner")
                print("Nothing selected in the outliner")

                return None
            
            return item_selected




    
    def apply_random_animation(self,
                               obj, duration, 
                               step, tx_min, ty_min, tz_min, tx_max, ty_max, tz_max, 
                               rx_min, ry_min, rz_min, rx_max, ry_max, rz_max, 
                               sx_min, sy_min, sz_min, sx_max, sy_max, sz_max):
        #ici on va créer la fonction qui applique une animation aléatoire
        # question est ce que les valeurs de tx, ty, tz, rx, ry, rz, sx, sy, sz    
        
        
        object = obj

        cmds.playbackOptions(min=1, max=duration) #on indique la longueur de l'animation en frame

        
        number_of_keys = duration // step # le // permet d'obtenir le résultat arrondie a l'infirrieur et sans décimale

        for i in range(number_of_keys + 1): #on ajoute +1 pour inclure la dernière frame
            current_frame = i * step
            cmds.currentTime(current_frame)

            random_translate_x = random.uniform(tx_min, tx_max)
            random_translate_y = random.uniform(ty_min, ty_max)
            random_translate_z = random.uniform(tz_min, tz_max)

            random_rotate_x = random.uniform(rx_min, rx_max)
            random_rotate_y = random.uniform(ry_min, ry_max)
            random_rotate_z = random.uniform(rz_min, rz_max)

            random_scale_x = random.uniform(sx_min, sx_max)
            random_scale_y = random.uniform(sy_min, sy_max)
            random_scale_z = random.uniform(sz_min, sz_max)

            cmds.setAttr(f"{object}.translateX", random_translate_x)
            cmds.setAttr(f"{object}.translateY", random_translate_y)
            cmds.setAttr(f"{object}.translateZ", random_translate_z)

            cmds.setAttr(f"{object}.rotateX", random_rotate_x)
            cmds.setAttr(f"{object}.rotateY", random_rotate_y)
            cmds.setAttr(f"{object}.rotateZ", random_rotate_z)

            cmds.setAttr(f"{object}.scaleX", random_scale_x)
            cmds.setAttr(f"{object}.scaleY", random_scale_y)
            cmds.setAttr(f"{object}.scaleZ", random_scale_z)

            cmds.setKeyframe(object)
    
    
        









    def on_click(self):
        
        if self.check_selection() is None: #si aucun item n'est selectionné, on quitte la fonction
            return

      #la fonction random value va me retourner les value dans cette ordre, on doit donc les mettre dans l'ordre return:
      # self.value_duration, self.value_step, 
      # self.random_translate_x, self.random_translate_y, self.random_translate_z, 
      # self.random_rotate_x, self.random_rotate_y, self.random_rotate_z, 
      # self.random_scale_x, self.random_scale_y, self.random_scale_z
      # t=translate, r=rotate, s=scale, x,y,z=axis

        (duration, step, tx_min, ty_min, tz_min, tx_max, ty_max, tz_max, rx_min, ry_min, rz_min, rx_max, ry_max, rz_max, sx_min, sy_min, sz_min, sx_max, sy_max, sz_max) = self.ui.get_value()

        for obj in self.check_selection(): #pour chaque objet selectionné, on va appliquer l'animation aléatoire
            self.apply_random_animation(obj, duration, step, tx_min, ty_min, tz_min, rx_min, ry_min, rz_min, sx_min, sy_min, sz_min)

        # a faire :
        # 1 -  chaque objet possède une frame de début et une frame de fin 
    #Créer une animation aléatoire s'appliquant uniquement aux objets sélectionnés.
    #Permettre de configurer la durée de l'animation ainsi que le nombre d'images entre chaque clé d'animation.
    #               fait # Pour chacun des paramètres de base (translation, rotation et échelle), permettre de définir lesvaleurs minimales et maximales pour chaque axe (X, Y, Z).
    # Permettre de régénérer l'animation afin de créer une nouvelle variation.
    # Prendre en charge la commande CTRL+Z (Undo).

        


    

    