#import de librairie classique/de base
import os
import sys

#voir les paths accessibles
print(sys.path)


# on a obtennue le fichier courrant : __file__
absolute_file_path = os.path.abspath(__file__) #donner le path du fichier en cours
print(absolute_file_path)


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
        animator_play.ui.deleteLater()
    except Exception:
        pass

    
    animator_play = ui.RandomAnimationUI() 
    # mon self.ui.show() est maintenant dans le init de la classe RandomAnimation, donc je n'ai pas besoin de le mettre ici sinon il pop en double
   
 
main() #call la fonction main
animator_play = animator.RandomAnimation() #on crée un objet de la classe RandomAnimation