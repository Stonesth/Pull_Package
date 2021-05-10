from Tools import tools_v000 as tools
import os
import sys
from os.path import dirname


# -12 for the name of this project Pull_Package
# save_path = dirname(__file__)[ : -12]
save_path = os.path.dirname(os.path.abspath("__file__"))[ : -12]
propertiesFolder_path = save_path + "\\"+ "Properties"

# Example of used
applications = tools.readProperty(propertiesFolder_path, 'Pull_Package', 'applications=')
applications_build = tools.readProperty(propertiesFolder_path, 'Pull_Package', 'applications_build=')

def pullPackage():
    try :
        pullPackageName = str(sys.argv[1])

        if pullPackageName != '' :
            print ('I can begin to pull the pachage : ' + pullPackageName )
           
            for app_name in applications.split(', '):
                try :
                    # Go to the folder of the application and the package
                    os.chdir(save_path + "\\" + app_name + "\\" + pullPackageName)
                    # print(os.getcwd())

                    os.system('git pull')

                    # Applications that I need to run the command : python setup.py build
                    if app_name in applications_build :
                        # Go to the folder of the application
                        os.chdir(os.path.join(save_path, app_name, "build", "exe.win-amd64-2.7") )
                        print(os.getcwd())
                        
                        # Remove the Directory
                        os.system('rmdir /q /s ' + pullPackageName)

                        # Go to the root folder of the application
                        os.chdir(save_path + "\\" + app_name)

                        # Run the command to build the application
                        os.system('python setup.py build')
                    
                    else :
                        print ("This project " + app_name + " don't need to be built") 

                except WindowsError as e2:
                    print ("This package " + pullPackageName + " is not existing in this project : " + app_name) 


                # Return to the current 
                os.chdir(save_path)
                # print(os.getcwd())


            
    except IndexError as e1:
        print ("You don't place a name for pull") 

pullPackage()