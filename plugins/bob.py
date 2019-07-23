import __main__ # To access MOPPA
import random # Only needed for the demonstration of MOPPA. You can remove it if your code doesn't need it

# Creating the class object
# It must be the same name as the file name (without .py)
class bob(object):
    # Defining a string, that will be accessed from  __main__ (moppa.py)
    ID = 'Bob_ID'
    _url = 'bob.dummy.site'

    def __init__(self):
        print('The plugin ' + self.ID + ' is being instantiated')

    def check_me(self):
        return random.choice([True, False])

    # Exemples of a function called with a parameter (param1)
    def login(self,param1):
        print(self.ID + ' : Starting login')
        print('Simulating a login to ' + self._url + ' with login=' + __main__.my_login + ' and password=' + __main__.my_password + ' and param:' + param1)
        # Exemple of changing value from plugin
        __main__.my_param1 = 'New value coming from bob'
        # Exemple of returning a value, coming from a function in MOPPA
        return __main__.moppa_dummy(self)