from Tools import tools_v000 as tools
import os
from os.path import dirname


# -12 for the name of this project Pull_Package
save_path = dirname(__file__)[ : -12]
propertiesFolder_path = save_path + "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'Pull_Package', 'user_text=')
