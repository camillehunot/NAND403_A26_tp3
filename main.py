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

def main(): #definition fonction main
    global widget #global permet que la variable widget est accessible partout, permet de garder la variable pour plus tard
    
    try: #permet de pas les accumuler plus d'une fois
        widget.close()
    except Exception:
        pass

    
    widget = ui.RandomAnimationUI() 
    widget.show()
 
main() #call la fonction main

