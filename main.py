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



from ui import MyClass

my_class = MyClass()
my_class.print_variable()