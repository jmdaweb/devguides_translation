# -*- coding: utf-8 -*-
documentation = [
_(u"""# Translating the gestures"""),
"",_(u"""The gestures defined originally in NVDA are adapted with English softwares and keyboard layout. In most cases, these gestures can also be executed on other keyboard layouts without any problem. However, sometimes a gesture originally defined by NVDA is not adapted for a specific locale (keyboard layout or software). The need to modify an original gesture may be due to the following reasons:"""),
"",_(u"""* The original gesture is defined with a character that is not a key name on the locale keyboard layout. Generally, the key names are the characters that can be input without the help of a modifier key (shift, control, etc.)"""),
_(u"""* The original gesture takes advantage of the keys physical location on the English keyboard layout, but this advantage does not appear anymore with the locale keyboard layout."""),
_(u"""* The original gesture is defined to match a native shortcut in Windows or in an application, but the shortcut in the local version of Windows or of this application is not the same as the English one."""),
"",_(u"""In all of this case, NVDA allows to remap this gesture for this specific locale."""),
"",_(u"""## Examples of modifications of a `gestures.ini` file"""),
"",_(u"""Below are three detailed examples of gestures.ini files corresponding to the three listed situations where a gesture remapping could be required."""),
"",_(u"""### Example 1: The original gesture is defined with a character that is not a key name on the locale keyboard layout"""),
"",_(u"""In English original version, the scripts for left and right mouse click (laptop layout) are executed respectively with NVDA+[ and NVDA+]. On English keyboard layout, the [ and ] keys are the two keys at the right of the P key."""),
_(u"""On Italian keyboard layout, [ and ] characters can only be input with the help of AltGr modifier: AltGr+è and AltGr+Plus respectively. Thus Italian translators decided to remap these scripts with the two keys at the right of the P key on Italian keyboard layout, i.e. è and +. To do this they have added the following lines in the `gestures.ini` file:"""),
"",_(u"""```"""),
_(u"""[globalCommands.GlobalCommands]"""),
_(u"""	leftMouseClick = kb(laptop):NVDA+è"""),
_(u"""	rightMouseClick = kb(laptop):NVDA+plus"""),
_(u"""```"""),
"",_(u"""### Example 2: The original gesture takes advantage of the keys physical location """),
"",_(u"""Looking again at the scripts for left and right mouse click (laptop layout) we can see that they are originally mapped (in English) to two neighboring keys. This reminds the left and right buttons of the mouse."""),
_(u"""As seen in example 1, many translators have had to modify these keys. Most of them (if not all) have chosen two neighboring keys. E.g. in French `gestures.ini` the following lines have been added:"""),
"",_(u"""```"""),
_(u"""[globalCommands.GlobalCommands]"""),
_(u"""	None = kb(laptop):nvda+[, kb(laptop):nvda+control+[, kb(laptop):nvda+], kb(laptop):nvda+control+], kb(laptop):nvda+shift+., kb(laptop):nvda+., kb(laptop):nvda+control+."""),
_(u"""	leftMouseClick = kb(laptop):nvda+ù"""),
_(u"""	rightMouseClick = kb(laptop):nvda+*"""),
_(u"""```"""),
"",_(u"""The ù and * on French layout are not at the same location as [ and ] of English layout, but these are still two neighboring keys."""),
_(u"""Moreover we can see here that NVDA+[ and NVDA+] has been among other mapped to None in order to unbind these gestures. For French (France) layout, this was not mandatory since there is no possibility to input NVDA+[ or NVDA+] without any other modifier key."""),
"",_(u"""### Example 3: The original gesture is defined to match a native shortcut"""),
"",_(u"""NVDA provides a script for Word document object named `toggleBold`. This script is mapped to the same gesture as the Word native shortcut to set text bold, i.e. Control+B in English version of Word. However on French version of Word, the shortcut to turn text bold is Control+G. The G stands for \"gras\" meaning \"bold\" in French. The following lines have been added in the French `gestures.ini` file to remap this script:"""),
"",_(u"""```"""),
_(u"""[NVDAObjects.window.winword.WordDocument]"""),
_(u"""	None = kb:control+b, kb:control+[, kb:control+], \"kb:control+shift+,\", kb:control+shift+., kb:control+l, kb:control+r"""),
_(u"""	toggleBold = kb:control+g, kb:control+shift+b"""),
_(u"""```"""),
"",_(u"""We can see that Control+B has been unbound. This was necessary because it is the shortcut of another command in French version of Word."""),
_(u"""No remapping has been done for toggleItalic script since the shortcut is the same for French and English versions of Word."""),
"",_(u"""## How to remap a shortcut key"""),
"",_(u"""### Identify the class, the script and the original gesture to be remapped"""),
"",_(u"""To edit the gesture.ini file, you will have to identify the class, the script and the original shortcut you want to remap."""),
"",_(u"""#### Case of a global command script"""),
"",_(u"""If the gesture to be remapped is a global command, you may execute the following steps to find out the class and the script name of the command:"""),
"",_(u"""* activate input help (NVDA+1)"""),
_(u"""* press the gesture you want to remap, e.g. NVDA+] (laptop layout)"""),
_(u"""* de-activate input help (NVDA+1)"""),
_(u"""* open the log (NVDA+F1)"""),
_(u"""* find out the line corresponding to the moment you have executed the gesture, e.g.:"""),
_(u"""  ```"""),
_(u"""  Input help: gesture kb(laptop):NVDA+], bound to script rightMouseClick on globalCommands.GlobalCommands"""),
_(u"""  ```"""),
"",_(u"""The information you are searching is on this line:"""),
"",_(u"""* script name: `rightMouseClick`"""),
_(u"""* class name: `globalCommands.GlobalCommands` (Note that this is always this class for global commands)"""),
_(u"""* original gesture: `kb(laptop):NVDA+]`"""),
"",_(u"""#### Case of an application specific script"""),
"",_(u"""In case you want to remap an application specific script, you will have to follow the same steps as those for a global command script. You just need to ensure before proceeding that you are in the targeted application."""),
"",_(u"""#### Case of an object specific script"""),
"",_(u"""Object specific scripts such as the ones linked to `NVDAObjects.window.winword.WordDocument` do not have generally an help message. So the previous technique will not work. You will need to explore NVDA's source code to find the class and the script name of the gesture you want to remap."""),
"",_(u"""### Edit the gestures.ini file"""),
"",_(u"""1. In your local copy of the screenReaderTranslations repository, check if the gestures.ini file exists, e.g. d:\\SVN\\SRT\\fr\\gestures.ini"""),
"",_(u"""   * If this file does not exist, create it by copying it from the last version of NVDA."""),
_(u"""   * If it already exists, all is fine."""),
"",_(u"""2. In this file the sections correspond to the class to which the script belongs. If the class your looking for does not exist, create this section."""),
_(u"""3. Under the targeted section, add a line corresponding to the new shortcut. E.g.:"""),
_(u"""   ```"""),
_(u"""   toggleBold = kb:control+g, kb:control+shift+b"""),
_(u"""   ```"""),
_(u"""   If a line already exists for the script name you want to modify the shortcut, add the new shortcut on the same line, separating each shortcut from another with a comma (,)"""),
_(u"""4. If you want to unmap the original shortcut, just map it to `None`, e.g.:"""),
_(u"""   ```"""),
_(u"""   None = kb:control+b"""),
_(u"""   ```"""),
_(u"""   Unmapping the original shortcut is only required if this shortcut does not match any other remapped locale shortcut."""),
_(u"""5. Save your file in UTF-8 format."""),
_(u"""6. Commit your changes to screenReaderTranslations repo."""),
"",_(u"""## What happens next"""),
"",_(u"""The automatic translation system will periodically copy the modified gestures.ini files from the screenReaderTranslations repo in the beta branch of the NVDA repo."""),
]