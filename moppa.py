# My Own Python Plugin Attempt (MOPPA)
#
# Yes, I like to give (stupid) names
#
# By Olivier Gaulard
# 
# The objective/concept is to have :
#   - Several "plugins" (Python Classes in fact) that are architectured in the same way (like a template)
#   - The code does not know in advance the names of the files (called plugins)
#   - It is just expecting some functions to be present, callable and returning values (if needed)
#   - One plugin that is used at a time (active_plugin). But it can be changed easily
#
# The structure is as follows : 
# moppa.py [This file]
# plugins/pluginA.py
# plugins/pluginB.py
# plugins/etc...
# 
# MOPPA will cycle through all the files in the plugins directory.
# You define your own way of selecting/identifying the correct plugin you want to work with (function check_me() in this exemple).
#
# You want to add a new plugin ? 
#   Just use the same template you have used for the others 
#   Put it into the plugin directory
#   Rescan

# In this demo, you will see some exemples of using/accessing variables, functions
# and passing some values between this file and the loaded plugin (and the other way around).

# Finally, I'm not a developper. MOPPA is just a way to have fun with Python and to (eventually) use it in another project

# 
#
# 

# Needed imports, but standard.
import os
import importlib
# Only needed for the demonstration of MOPPA. You can remove it if your code doesn't need it
import random 

# Defining some variables that will can be accessed by the active_plugin
my_login='Robert'
my_password ='12345'
my_param1 = 'param_from_moppa'

# Exemple of a function that will be called from the active_plugin
def moppa_dummy(self):
    return random.choice([True, False])

# Flag to track result of check_me() function (see below and in the plugins files)
active_flag = False
# Defining the directory name where plugins are located
class_path = 'plugins'

# Getting the path of this Python file
# On Windows machine it will look like this : c:\moppa
# On Linux machine, it will look like this : /home
my_path = os.path.dirname(os.path.realpath(__file__))
# Adding slashes and plugin directory to get full path
# Since it cand depend on the environement (Windows or Linux), let's rely on the os.path.sep function
my_path += os.path.sep + class_path + os.path.sep
print('Final Path :' + my_path)

# Starting the 'for' loop to list all files in the directory 'my_path'
for plugin in os.listdir(my_path):
    # Filtering some files and directories. If you want to add more filters, you can just add : 
    # or plugin == 'dont_consider_me.py'
    if plugin == '__init__.py' or plugin[-3:] != '.py' :
        # Skipping those files
        continue
    print(plugin)
    
    # The overall goal of the folling 3 lines of code, is to do the same as those 2 (alice being an exemple): 
    # from plugins.alice import alice
    # active_plugin = alice()

    # When found, importing the plugin (called 'module' in the function's name below)
    new_plugin = importlib.import_module(class_path + '.' + plugin[:-3])
    # Get the attribute of the class 'plugin' from the object 'new_plugin'
    my_new = getattr(new_plugin, plugin[:-3])
    # Let's instantiate the selected plugin/class
    active_plugin = my_new()

    # Exemple of getting a returned value from the active_plugin function check_me()
    if active_plugin.check_me():
        # Exemple of directly fetching a value defined inside the active_plugin
        print('True returned from ' + active_plugin.ID)
        # Setting flag to True to indicate check_me is OK
        active_flag = True
        # Stop searching by breaking out of the 'for' loop
        break
    else:
        print('False returned from ' + active_plugin.ID)

# Out of the 'For' loop, but do we have an 'active_plugin' defined ?         
if active_flag:
    # Exemple of passing a parameter (my_param1) to a called function (.login) of the active_plugin
    result = active_plugin.login(my_param1)
    print('Result of the login function : ' + str(result))
    # Exemple of a string being updated by active_plugin (see plugin code)
    print('my_param1 value: ' + my_param1)
else:
    # Since it is using random, don't hesitate to run MOPPA several times
    print('No plugin selected')