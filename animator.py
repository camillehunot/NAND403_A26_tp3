import os
import random
import sys

from maya import cmds
from PySide6.QtWidgets import ( QMessageBox, )

class RandomAnimation:
    def __init__(self):
         super().__init__() 
      


    def check_selection(self, no_selection):
    
            item_selected= cmds.ls(selection=True) #permet de récupérer les objets selectionnés dans maya et de les mettre dans la variable item_selected
        
            if not item_selected: #si aucun item n'est selectionné, on affiche un message d'erreur
                no_selection()
            #     QMessageBox.warning(self.ui, "Warning", "Nothing selected in the outliner")
            #     print("Nothing selected in the outliner")
                return None
            
            return item_selected


    def apply_random_animation(self,
                               obj, duration, 
                               step, tx_min, ty_min, tz_min, tx_max, ty_max, tz_max, 
                               rx_min, ry_min, rz_min, rx_max, ry_max, rz_max, 
                               sx_min, sy_min, sz_min, sx_max, sy_max, sz_max):
        #ici on va créer la fonction qui applique une animation aléatoire
        
        #étape 1 : supprimer les clés déjà présentes
        cmds.cutKey(obj, time=(0, duration), attribute=["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ", "scaleX", "scaleY", "scaleZ"])
        
        
        cmds.playbackOptions(min=1, max=duration) #on indique la longueur de l'animation en frame
        start_frame = 0
        end_frame = start_frame + duration
        number_of_keys = duration // step # le // permet d'obtenir le résultat arrondie a l'infirrieur et sans décimale


        # ici on créé des variables pour stocker les valeurs de départ de l'objet, pour pouvoir copier a la dernière frame
        start_tx, start_ty, start_tz = None, None, None
        start_rx, start_ry, start_rz = None, None, None
        start_sx, start_sy, start_sz = None, None, None 


        for i in range(number_of_keys): #on ajoutera la dernière frame plus tard
                
            current_frame = i * step #permet de savoir a quelle frame on doit mettre la key

        #-------- prendre une valeur aléatoire
            random_t_x = random.uniform(tx_min, tx_max)
            random_t_y = random.uniform(ty_min, ty_max)
            random_t_z = random.uniform(tz_min, tz_max)

            random_r_x = random.uniform(rx_min, rx_max)
            random_r_y = random.uniform(ry_min, ry_max)
            random_r_z = random.uniform(rz_min, rz_max)

            random_s_x = random.uniform(sx_min, sx_max)
            random_s_y = random.uniform(sy_min, sy_max)
            random_s_z = random.uniform(sz_min, sz_max)

    
         #-------- on set la key 
            self.set_maya_keys(obj, current_frame, 
                               random_t_x, random_t_y, random_t_z, 
                               random_r_x, random_r_y, random_r_z, 
                               random_s_x, random_s_y, random_s_z)



         #-------- si c'est la première frame on sauvegarde les valeurs
            if current_frame == start_frame: #si on est a la première frame, on met les valeurs de base de l'objet
                start_tx, start_ty, start_tz = random_t_x, random_t_y, random_t_z
                start_rx, start_ry, start_rz = random_r_x, random_r_y, random_r_z
                start_sx, start_sy, start_sz = random_s_x, random_s_y, random_s_z



         #-------- on copie les valeur du début de l'animation a la fin pour que cela loop
        self.set_maya_keys(obj, end_frame, 
                           start_tx, start_ty, start_tz, 
                           start_rx, start_ry, start_rz, 
                           start_sx, start_sy, start_sz)

        
        

    
    def set_maya_keys(self, obj, current_frame, random_t_x, random_t_y, random_t_z, random_r_x, random_r_y, random_r_z, random_s_x, random_s_y, random_s_z):

        cmds.setKeyframe(obj, attribute="translateX", value=random_t_x, time=current_frame)
        cmds.setKeyframe(obj, attribute="translateY", value=random_t_y, time=current_frame)
        cmds.setKeyframe(obj, attribute="translateZ", value=random_t_z, time=current_frame)

        cmds.setKeyframe(obj, attribute="rotateX", value=random_r_x, time=current_frame)
        cmds.setKeyframe(obj, attribute="rotateY", value=random_r_y, time=current_frame)
        cmds.setKeyframe(obj, attribute="rotateZ", value=random_r_z, time=current_frame)

        cmds.setKeyframe(obj, attribute="scaleX", value=random_s_x, time=current_frame)
        cmds.setKeyframe(obj, attribute="scaleY", value=random_s_y, time=current_frame)
        cmds.setKeyframe(obj, attribute="scaleZ", value=random_s_z, time=current_frame)




    def on_click(self, duration, step, 
                 tx_min, ty_min, tz_min,
                 tx_max, ty_max, tz_max, 
                 rx_min, ry_min, rz_min, 
                 rx_max, ry_max, rz_max, 
                 sx_min, sy_min, sz_min, 
                 sx_max, sy_max, sz_max, no_selection
                 ):


        selection = self.check_selection(no_selection)
        

        if selection is None: #si aucun item n'est selectionné, on quitte la fonction
            return

    
        cmds.undoInfo(openChunk=True)

        try:
            for obj in selection: #pour chaque objet selectionné, on va appliquer l'animation aléatoire
                self.apply_random_animation(obj, duration, step, 
                                            tx_min, ty_min, tz_min, 
                                            tx_max, ty_max, tz_max, 
                                            rx_min, ry_min, rz_min, 
                                            rx_max, ry_max, rz_max, 
                                            sx_min, sy_min, sz_min, 
                                            sx_max, sy_max, sz_max)

        except:
            pass


        finally:
            cmds.undoInfo(closeChunk=True)




        


    

    