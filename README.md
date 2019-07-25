My Own Python Plugin Attemp (MOPPA)

The objective/concept is to have :
   - Several "plugins" (Python Classes in fact) that are architectured in the same way (like a template)
   - The code does not know in advance the names of the files (called plugins)
   - It is expecting some functions to be present, callable and returning values (if needed)
   - One plugin that is used at a time (active_plugin). But this can be changed easily

The structure is as follows : 
- moppa.py
- plugins/pluginA.py
- plugins/pluginB.py
- plugins/etc...
 
MOPPA will cycle through all the files in the plugins directory.
You define your own way of selecting/identifying the correct plugin you want to work with (function check_me() in this exemple).

You want to add a new plugin ? 
- Just use the same template you have used for the others 
- Put it into the plugin directory
- Rescan

In this demo, you will see some exemples of using/accessing variables, functions and passing some values between this file and the loaded plugin (and the other way around).

Finally, I'm not a developper. MOPPA is just a way to have fun with Python and to (eventually) use it in another project.
