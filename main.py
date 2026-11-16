#import de librairie classique/de base
import os
import sys


# on a obtennue le fichier courrant : __file__
absolute_file_path = os.path.abspath(__file__) #donner le path du fichier en cours

#On trouve le path du folder
absolute_folder_path = os.path.dirname(absolute_file_path)


#ajouter le absolute_folder_path au path de python pour qu'il puisse trouver le path
sys.path.append(absolute_folder_path)

#################################################################################

import importlib
import ui
importlib.reload(ui).RandomAnimationUI

import importlib
import animator
importlib.reload(animator)

def main(): #definition fonction main
 
    global animator_play #global permet que la variable animator_play est accessible partout, permet de garder la variable pour plus tard
    
    try: #permet de pas les accumuler plus d'une fois
        
        animator_play.ui.close()
      
    except Exception:
        pass

    variable_animation = animator.RandomAnimation()
    
    animator_play = ui.RandomAnimationUI(variable_animation) 
   

    animator_play.show()

 
main() #call la fonction main
