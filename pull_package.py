from Tools import tools_v000 as tools
import os
import sys
from os.path import dirname


# -12 for the name of this project Pull_Package
# save_path = dirname(__file__)[ : -12]
save_path = os.path.dirname(os.path.abspath("__file__"))[ : -12]
propertiesFolder_path = save_path + "\\"+ "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'Pull_Package', 'user_text=')

def pullPackage():
    try :
        pullPackageName = str(sys.argv[1])

        if pullPackageName != '' :
            print ('I can begin to pull the pachage : ' + pullPackageName )
            
    except IndexError as e1:
        print ("You don't place a name for pull") 

pullPackage()