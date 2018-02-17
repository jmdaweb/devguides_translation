---
generator: 'http://txt2tags.sf.net'
title: 'NVDA 2017.4 Developer Guide'
---

NVDA 2017.4 Developer Guide
===========================

[]{#toc}

Table of Contents
-----------------

-   [1. Introduction](#toc2)
    -   [1.1. A Note About Python](#toc3)
-   [2. Translation](#toc4)
    -   [2.1. Character Descriptions](#toc5)
    -   [2.2. Symbol Pronunciation](#toc6)
        -   [2.2.1. Defining Complex Symbols](#toc7)
        -   [2.2.2. Defining Symbol Information](#toc8)
-   [3. Plugins](#toc9)
    -   [3.1. Overview](#toc10)
    -   [3.2. Types of Plugins](#toc11)
    -   [3.3. Basics of an App Module](#toc12)
    -   [3.4. Example 1: An App Module that Beeps on Focus Change
        Events](#Example1)
    -   [3.5. Basics of a Global Plugin](#toc14)
    -   [3.6. Example 2: a Global Plugin Providing a Script to Announce
        the NVDA Version](#toc15)
    -   [3.7. NVDA Objects](#toc16)
    -   [3.8. Scripts and Gesture Bindings](#toc17)
    -   [3.9. Example 3: A Global Plugin to Find out Window Class and
        Control ID](#toc18)
    -   [3.10. Events](#toc19)
    -   [3.11. the App Module SleepMode variable](#toc20)
    -   [3.12. Example 4: A Sleep Mode App Module](#toc21)
    -   [3.13. Providing Custom NVDA Object Classes](#toc22)
    -   [3.14. Example 5: Command to Retrieve the Length of Text in an
        Edit Field Using a Custom NVDA Object](#toc23)
    -   [3.15. Making Small Changes to an NVDA Object in App
        Modules](#toc24)
    -   [3.16. Example 6: Labelling the Notepad Edit Field Using
        event\_NVDAObject\_init](#toc25)
-   [4. Packaging Code as NVDA Add-ons](#toc26)
    -   [4.1. Non-ASCII File Names in Zip Archives](#toc27)
    -   [4.2. Manifest Files](#toc28)
        -   [4.2.1. Available Fields](#toc29)
        -   [4.2.2. An Example Manifest File](#toc30)
    -   [4.3. Plugins and Drivers](#toc31)
    -   [4.4. Optional install / Uninstall code](#toc32)
        -   [4.4.1. the onInstall function](#toc33)
        -   [4.4.2. The onUninstall Function](#toc34)
    -   [4.5. Localizing Add-ons](#toc35)
        -   [4.5.1. Locale-specific Manifest Files](#toc36)
        -   [4.5.2. Locale-specific Messages](#toc37)
    -   [4.6. Add-on Documentation](#AddonDoc)
-   [5. NVDA Python Console](#PythonConsole)
    -   [5.1. Usage](#toc40)
    -   [5.2. Namespace](#PythonConsoleNamespace)
        -   [5.2.1. Automatic Imports](#toc42)
        -   [5.2.2. Snapshot Variables](#PythonConsoleSnapshotVariables)
-   [6. Remote Python Console](#toc44)
    -   [6.1. Usage](#toc45)

[]{#toc2}

1. Introduction
---------------

This guide provides information concerning NVDA development, including
translation and the development of components for NVDA.

[]{#toc3}

### 1.1. A Note About Python

NVDA and its components are primarily written in the Python programming
language. It is not the goal of this guide to teach you Python, though
examples are provided through out this guide which will help to
familiarise you with the Python syntax. Documentation and other
resources related to the Python language can be found at
[www.python.org/](http://www.python.org/)

[]{#toc4}

2. Translation
--------------

In order to support multiple languages/locales, NVDA must be translated
and data specific to the locale must be provided. This section only
includes information on custom NVDA file formats required for
translation. Other items need to be translated, such as the NVDA user
interface and documentation, but these use standard file formats. For
complete documentation about translating NVDA, please see
<https://github.com/nvaccess/nvda/wiki/Translating>

[]{#toc5}

### 2.1. Character Descriptions

Sometimes, it can be very difficult or even impossible to distinguish
one character from another. For example, two characters might be
pronounced the same way, even though they are actually different
characters. To help users when this occurs, character descriptions can
be provided which describe the character in a unique way.

Character descriptions can be provided for a locale in a file named
characterDescriptions.dic in the directory for the locale. This is a
UTF-8 encoded text file. Blank lines and lines beginning with a \"\#\"
character are ignored. All other lines should contain a character,
followed by a tab, then one or more descriptions separated by tabs.

For example:

    # This is a comment.
    a   alpha
    b   bravo

See the file locale\\en\\characterDescriptions.dic for a full example.

In most cases, the characters in this file should be a single lower case
character. It is assumed that characters will have the same description
regardless of their case, so upper case characters are converted to
lower case before looking up their character descriptions.

[]{#toc6}

### 2.2. Symbol Pronunciation

It is often useful to hear punctuation and other symbols pronounced as
words when reading text, particularly when moving by character.
Unfortunately, the pronunciation of symbols is inconsistent between
speech synthesisers and many synthesisers do not speak many symbols
and/or do not allow control over what symbols are spoken. Therefore,
NVDA allows information about symbol pronunciation to be provided.

This is done for a locale by providing a file named symbols.dic in the
directory for the locale. This is a UTF-8 encoded text file. Blank lines
and lines beginning with a \"\#\" character are ignored. All locales
implicitly inherit the symbol information for English, though any of
this information can be overridden.

The file contains two sections.

[]{#toc7}

#### 2.2.1. Defining Complex Symbols

The first section is optional and defines regular expression patterns
for complex symbols. Complex symbols are symbols which aren\'t simply a
character or sequence of characters, but instead require a more
complicated match. An example is the full stop (.) sentence ending in
English. The \".\" is used for multiple purposes, so a more complicated
check is required to determine whether this refers to the end of a
sentence.

The complex symbols section begins with the line:

    complexSymbols:

Subsequent lines contain a textual identifier used to identify the
symbol, a tab and the regular expression pattern for that symbol. For
example:

    . sentence ending   (?<=[^\s.])\.(?=[\"')\s]|$)

Again, the English symbols are inherited by all other locales, so you
need not include any complex symbols already defined for English.

[]{#toc8}

#### 2.2.2. Defining Symbol Information

The second section provides information about when and how to pronounce
all symbols. It begins with the line:

    symbols:

Subsequent lines should contain several fields separated by tabs. The
only mandatory fields are the identifier and replacement. The default
will be used for omitted fields. The fields are as follows:

-   identifier: The identifier of the symbol. In most cases, this is
    just the character or characters of the symbol. However, it can also
    be the identifier of a complex symbol. Certain characters cannot be
    typed into the file, so the following special sequences can be used:
    -   \\0: null
    -   \\t: tab
    -   \\n: line feed
    -   \\r: carriage return
    -   \\f: form feed
    -   \\\#: \# character (needed because \# at the start of a line
        denotes a comment)
-   replacement: The text which should be spoken for the symbol.
-   level: The symbol level at which the symbol should be spoken. The
    symbol level is configured by the user and specifies the amount of
    symbols that should be spoken. This field should contain one of the
    levels \"none\", \"some\", \"most\", \"all\" or \"char\", or \"-\"
    to use the default. \"char\" means that the symbol should only be
    pronounced when moving by character. The default is to inherit the
    value or \"all\" if there is nothing to inherit.
-   preserve: Whether the symbol itself should be preserved to
    facilitate correct pronunciation by the synthesiser. For example,
    symbols which cause pauses or inflection (such as the comma in
    English) should be preserved. This field should be one of the
    following:
    -   never: Never preserve the symbol.
    -   always: Always preserve the symbol.
    -   norep: Only preserve the symbol if it is not being replaced;
        i.e. the user has set symbol level lower than the level of this
        symbol.
    -   -: Use the default.

    The default is to inherit the value or \"never\" if there is nothing
    to inherit.

Finally, a display name for the symbol can be provided in a comment
after a tab at the end of the line. This will be shown to users when
editing the symbol information and is especially useful for translators
to define translated names for English complex symbols.

Here are some examples:

    (   left paren  most

This means that the \"(\" character should be spoken as \"left paren\"
only when the symbol level is set to most or higher; i.e. most or all.

    ,   comma   all always

This means that the \",\" character should be spoken as \"comma\" when
the symbol level is set to all and that the character itself should
always be preserved so that the synthesiser will pause appropriately.

    . sentence ending   point   # . fin de phrase

This line appears in the French symbols.dic file. It means that the \".
sentence ending\" complex symbol should be spoken as \"point\". Level
and preserve are not specified, so they will be taken from English. A
display name is provided so that French users will know what the symbol
represents.

Please see the file locale\\en\\symbols.dic for the English definitions
which are inherited for all locales. This is also a good full example.

[]{#toc9}

3. Plugins
----------

[]{#toc10}

### 3.1. Overview

Plugins allow you to customize the way NVDA behaves overall or within a
particular application. They are able to:

-   Respond to particular events such as focus and object property
    changes; e.g. when a control changes its name.
-   Implement commands which are bound to particular key presses or
    other input.
-   Customise the behaviour of and implement additional functionality
    for particular controls.
-   Customise or add new support for text content and complex documents.

This section provides an introduction to developing plugins. Developers
should consult the code documentation for a complete reference.

[]{#toc11}

### 3.2. Types of Plugins

There are two types of plugins. These are:

-   App Modules: code specific to a particular application. The App
    Module receives all events for a particular application, even if
    that application is not currently active. When the application is
    active, any commands that the App Module has bound to key presses or
    other input can be executed by the user.
-   Global Plugins: code global to NVDA; i.e. it is used in all
    applications. Global Plugins Receive all events for all controls in
    the Operating System. Any commands bound by a Global Plugin can be
    executed by the user wherever they are in the operating system,
    regardless of application.

If you wish to improve NVDA\'s access to a particular application, it is
most likely you will want to write an App Module. In contrast, if you
wish to add some overall functionality to NVDA (e.g. a script that
announces current Wireless network strength while in any application),
then a Global Plugin is what you want.

Both App Modules and Global Plugins share a common look and feel. They
are both Python source files (with a .py extension), they both define a
special class containing all events, scripts and bindings, and they both
may define custom classes to access controls, text content and complex
documents. However, they do differ in some ways.

The following few sections will talk separately about App Modules and
Global Plugins. After this point, discussion is again more general.

[]{#toc12}

### 3.3. Basics of an App Module

App Module files have a .py extension, and are named the same as the
main executable of the application for which you wish them to be used.
For example, an App Module for notepad would be called notepad.py, as
notepad\'s main executable is called notepad.exe.

App Module files must be placed in the appModules subdirectory of the
user\'s NVDA user configuration directory. For more information on where
to find the user configuration directory, please see the NVDA user
guide.

App Modules must define a class called AppModule, which inherits from
appModuleHandler.AppModule. This class can then define event and script
methods, gesture bindings and other code. This will all be covered in
depth later.

NVDA loads an App Module for an application as soon as it notices the
application is running. The App Module is unloaded once the application
is closed or when NVDA is exiting.

[]{#Example1}

### 3.4. Example 1: An App Module that Beeps on Focus Change Events

The following example App Module makes NVDA beep each time the focus
changes within the notepad application. This example shows you the basic
layout of an App Module.

Copy and paste the code between (but not including) the start and end
markers into a new text file called notepad.py, which should be saved in
the AppModules subdirectory. Be very careful to keep all tabs and spaces
intact.

Once saved in the correct location, either restart NVDA or choose Reload
Plugins found under Tools in the NVDA menu.

Finally, open Notepad and move the focus around the application; e.g.
move along the menu bar, open some dialog boxes, etc. You should hear
beeps each time the focus changes. Note though that if you move outside
of Notepad - for instance, to Windows Explorer - you do not hear beeps.

    --- start ---
    # Notepad App Module for NVDA
    # Developer guide example 1

    import appModuleHandler

    class AppModule(appModuleHandler.AppModule):

        def event_gainFocus(self, obj, nextHandler):
            import tones
            tones.beep(550, 50)
            nextHandler()

    --- end ---

This App Module file starts with two comment lines, which describe what
the file is for.

It then imports the appModuleHandler module, so that the App Module then
has access to the base AppModule class.

Next, it defines a class called AppModule, which is inherited from
appModuleHandler.AppModule.

Inside this class, it defines 1 or more events, scripts or gesture
bindings. In this example, it defines one event method for gainFocus
events (event\_gainFocus), which plays a short beep each time it is
executed. The implementation of this event is not important for the
purposes of this example. The most important part is the class itself.
Events will be covered in greater detail later.

As with other examples in this guide, remember to delete the created app
module when you are finished testing and then restart NVDA or reload
plugins, so that original functionality is restored.

[]{#toc14}

### 3.5. Basics of a Global Plugin

Global Plugin files have a .py extension, and should have a short unique
name which identifies what they do.

Global Plugin files must be placed in the globalPlugins subdirectory of
the user\'s NVDA user configuration directory. For more information on
where to find the user configuration directory, please see the NVDA user
guide.

Global Plugins must define a class called GlobalPlugin, which inherits
from globalPluginHandler.GlobalPlugin. This class can then define event
and script methods, gesture bindings and other code. This will all be
covered in depth later.

NVDA loads all global plugins as soon as it starts, and unloads them on
exit.

[]{#toc15}

### 3.6. Example 2: a Global Plugin Providing a Script to Announce the NVDA Version

The following example Global Plugin Allows you to press NVDA+shift+v
while anywhere in the Operating System to find out NVDA\'s version. This
example is only to show you the basic layout of a Global Plugin.

Copy and paste the code between (but not including) the start and end
markers into a new text file with a name of example2.py, which should be
saved in the globalPlugins subdirectory. Be very careful to keep all
tabs and spaces intact.

Once saved in the right place, either restart NVDA or choose Reload
Plugins found under Tools in the NVDA menu.

From anywhere, you can now press NVDA+shift+v to have NVDA\'s version
spoken and brailled.

    --- start ---
    # Version announcement plugin for NVDA
    # Developer guide example 2

    import globalPluginHandler
    import ui
    import versionInfo

    class GlobalPlugin(globalPluginHandler.GlobalPlugin):

        def script_announceNVDAVersion(self, gesture):
            ui.message(versionInfo.version)

        __gestures={
            "kb:NVDA+shift+v": "announceNVDAVersion",
        }

    --- end ---

This Global Plugin file starts with two comment lines, which describe
what the file is for.

It then imports the globalPluginHandler module, so that the Global
Plugin has access to the base GlobalPlugin class.

It also imports a few other modules, namely ui and versionInfo, which
this specific plugin needs in order for it to perform the necessary
actions to announce the version.

Next, it defines a class called GlobalPlugin, which is inherited from
globalPluginHandler.GlobalPlugin.

Inside this class, it defines 1 or more events, scripts or gesture
bindings. In this example, it defines a script method that performs the
version announcement, and provides a binding from NVDA+shift+v to this
script. However, the details of the script and its binding are not
important for the purposes of this example. The most important part is
the class itself.

As with other examples in this guide, remember to delete the created
Global Plugin when finished testing and then restart NVDA or reload
plugins, so that original functionality is restored.

[]{#toc16}

### 3.7. NVDA Objects

NVDA represents controls and other GUI elements as NVDA Objects. These
NVDA Objects contain standardised properties, such as name, role, value,
states and description, which allow other parts of NVDA to query or
present information about a control in a generalised way. For example,
the OK button in a dialog would be represented as an NVDA Object with a
name of \"OK\" and a role of button. Similarly, a checkbox with a label
of \"I agree\" would have a name of \"I agree\", a role of checkbox, and
if currently checked, a state of checked.

As there are many different GUI Toolkits and platform and accessibility
APIs, NVDA Objects abstract these differences into a standard form that
NVDA can use, regardless of the toolkit or API a particular control is
made with. For example, the Ok button just discussed could be a widget
in a Java application, an MSAA object, an IAccessible2 object or a UI
Automation element.

NVDA Objects have many properties. Some of the most useful are:

-   name: the label of the control.
-   role: one of the ROLE\_\* constants from NVDA\'s controlTypes
    module. Button, dialog, editableText, window and checkbox are
    examples of roles.
-   states: a set of 0 or more of the STATE\_\* constants from NVDA\'s
    controlTypes module. Focusable, focused, selected, selectable,
    expanded, collapsed and checked are some examples of states.
-   value: the value of the control; e.g. the percentage of a scroll bar
    or the current setting of a combo box.
-   description: a sentence or two describing what the control does
    (usually the same as its tooltip).
-   location: the object\'s left, top, width and height positions in
    screen coordinates.
-   parent: this object\'s parent object. For example, a list item
    object\'s parent would be the list containing it.
-   next: the object directly after this one on the same level in
    logical order. For example, a menu item NVDA Object\'s next object
    is most likely another menu item within the same menu.
-   previous: like next but in reverse.
-   firstChild: the first direct child object of this object. For
    example, a list\'s first child would be the first list item.
-   lastChild: the last direct child of this object.
-   children: a list of all the direct children of this object; e.g. all
    the menu items in a menu.

There are also a few simplified navigation properties such as
simpleParent, simpleNext, simpleFirstChild and simpleLastChild. These
are like their respective navigation properties described above, but
NVDA filters out unuseful objects. These properties are used when
NVDA\'s simple review mode is turned on, which is the default. These
simple properties may be easier to use, but the real navigation
properties more closely reflect the underlying Operating System
structure. Also, these may change in future versions of NVDA as
improvements are made to simple review, so they should generally be
avoided when programmatically locating specific objects.

When developing plugins, most of the time, it is not important what
toolkit or API backs an NVDA Object, as the plugin will usually only
access standard properties such as name, role and value. However, as
plugins become more advanced, it is certainly possible to delve deeper
into NVDA Objects to find out toolkit or API specific information if
required.

Plugins make use of NVDA Objects in three particular ways:

-   Most events that plugins receive take an argument which is the NVDA
    Object on which the event occurred. For example, event\_gainFocus
    takes the NVDA Object that represents the control gaining focus.
-   Scripts, events or other code may fetch objects of interest such as
    the NVDA Object with focus, NVDA\'s current navigator object, or
    perhaps the Desktop NVDA Object. The code may then retreave
    information from that object or perhaps even retreave another object
    related to it (e.g. its parent, first child, etc.).
-   the Plugin may define its own custom NVDA Object classes which will
    be used to wrap a specific control to give it extra functionality,
    mutate its properties, etc.

Just like App Modules and Global Plugins, NVDA Objects can also define
events, scripts and gesture bindings.

[]{#toc17}

### 3.8. Scripts and Gesture Bindings

App Modules, Global Plugins and NVDA Objects can define special methods
which can be bound to a particular piece of input such as a key press.
NVDA refers to these methods as scripts.

A script is a standard Python instance method with a name starting with
\"script\_\"; e.g. \"script\_sayDateTime\".

A script method takes two arguments:

-   self: a reference to the App Module, Global Plugin or NVDA Object
    instance the script was called on.
-   gesture: an Input Gesture object, which represents the input that
    caused the script to run.

As well as the actual script method, some form of gesture binding must
be defined, so that NVDA knows what input should execute the script.

To bind a gesture to a script, a special \"\_\_gestures\" Python
dictionary can be defined as a class variable on the App Module, Global
Plugin or NVDA Object. These dictionaries should contain gesture
identifier strings pointing to the name of the requested script, without
the \"script\_\" prefix.

There are more advanced ways of binding gestures in a more dynamic
fashion, though the \_\_gestures dictionary is the simplest.

A gesture identifier string is a simple string representation of a piece
of input. It consists of a two leter character code denoting the source
of the input, an optional device in brackets, a colon (:) and one or
more names separated by a plus (+) denoting the actual keys or input
values.

Some examples of gesture string identifiers are:

-   \"kb:NVDA+shift+v\"
-   \"br(freedomScientific):leftWizWheelUp\"
-   \"kb(laptop):NVDA+t\"

Currently, the input sources in NVDA are:

-   kb: system keyboard input
-   br: braille display controls
-   ts: touch screen
-   bk: braille keyboard input

When NVDA receives input, it looks for a matching gesture binding in a
particular order. Once a gesture binding is found, the script is
executed and no further bindings are used, nore is that particular
gesture passed on automatically to the Operating System.

The order for gesture binding lookup is:

-   Loaded Global Plugins
-   App Module of the active application
-   Tree Interceptor of the NVDA Object with focus if any; e.g. a
    virtualBuffer
-   NVDA Object with focus
-   Global Commands (built in commands like quitting NVDA, object
    navigation commands, etc.)

You should specify a description of the script in the function\'s
docstring which describes the command for users. For example, this is
reported to users when in Input Help mode and shown in the Input
Gestures dialog. You specify the docstring by setting a
\"[doc]{.underline}\" attribute on the script function. The script will
not appear in the Input Gestures dialog unless this is specified.

You can also specify a category for a script so that it can be grouped
with other similar scripts. For example, a script in a global plugin
which adds browse mode quick navigation keys may be categorized under
the \"Browse mode\" category. For individual scripts, this is done by
setting a \"category\" attribute on the script function to a string
containing the name of the category. You can also set the
\"scriptCategory\" attribute on the plugin class, which will be used for
scripts which do not specify a category. There are constants for common
categories prefixed with SCRCAT\_ in the inputCore and globalCommands
modules. The script will be listed under the specified category in the
Input Gestures dialog. If no category is specified, the script will be
categorized under \"Miscellaneous\".

[]{#toc18}

### 3.9. Example 3: A Global Plugin to Find out Window Class and Control ID

The following Global Plugin allows you to press NVDA+leftArrow to have
the window class of the current focus announced, and NVDA+rightArrow to
have the window control ID of the current focus announced. This example
shows you how to define one or more scripts and gesture bindings on a
class such as an App Module, Global Plugin or NVDA Object.

Copy and paste the code between (but not including) the start and end
markers into a new text file with a name of example3.py, which should be
saved in the globalPlugins subdirectory. Be very careful to keep all
tabs and spaces intact.

Once saved in the right place, either restart NVDA or choose Reload
Plugins found under Tools in the NVDA menu.

    --- start ---
    #Window utility scripts for NVDA
    #Developer guide example 3

    import globalPluginHandler
    import ui
    import api

    class GlobalPlugin(globalPluginHandler.GlobalPlugin):

        def script_announceWindowClassName(self, gesture):
            focusObj = api.getFocusObject()
            name = focusObj.name
            windowClassName = focusObj.windowClassName
            ui.message("class for %s window: %s" % (name, windowClassName))

        def script_announceWindowControlID(self, gesture):
            focusObj = api.getFocusObject()
            name = focusObj.name
            windowControlID = focusObj.windowControlID
            ui.message("Control ID for %s window: %d" % (name, windowControlID))

        __gestures = {
            "kb:NVDA+leftArrow": "announceWindowClassName",
            "kb:NVDA+rightArrow": "announceWindowControlID",
        }

    --- end ---

[]{#toc19}

### 3.10. Events

When NVDA detects particular toolkit, API or Operating System events, it
abstracts these and fires its own internal events on plugins and NVDA
Objects.

Although most events are related to a specific NVDA Object (e.g. name
change, gain focus, state change, etc.), these events can be handled at
various levels. When an event is handled, it is stopped from going
further down the chain. However, code inside the event can choose to
propagate it further if needed.

The order of levels through which the event passes until an event method
is found is:

-   Loaded Global Plugins
-   The App Module associated with the NVDA Object on which the event
    was fired
-   The Tree Interceptor (if any) associated with the NVDAObject on
    which the event was fired
-   the NVDAObject itself.

Events are Python instance methods, with a name starting with
\"event\_\" followed by the actual name of the event (e.g. gainFocus).

These event methods take slightly different arguments depending at what
level they are defined.

If an event for an NVDA Object is defined on an NVDA Object itself, the
method only takes one mandatory argument which is the \'self\' argument;
i.e. the NVDA Object instance). Some events may take extra arguments,
though this is quite rare.

If an event for an NVDA Object is defined on a Global Plugin, App Module
or Tree Interceptor, the event takes the following arguments:

-   self: the instance of the Global Plugin, App Module or Tree
    Interceptor
-   obj: the NVDA Object on which the event was fired
-   nextHandler: a function that when called will propagate the event
    further down the chain.

Some common NVDA Object events are:

-   foreground: this NVDA Object has become the new foreground object;
    i.e. active top-level object
-   gainFocus
-   focusEntered: Focus has moved inside this object; i.e. it is an
    ancestor of the focus object
-   loseFocus
-   nameChange
-   valueChange
-   stateChange
-   caret: when the caret (insertion point) within this NVDA Object
    moves
-   locationChange: physical screen location changes

There are many other events, though those listed above are usually the
most useful.

For an example of an event handled by an App Module, please refer to
[example 1](#Example1) (focus beeps in notepad).

[]{#toc20}

### 3.11. the App Module SleepMode variable

App Modules have one very useful property called \"sleepMode\", which if
set to true almost completely disables NVDA within that application.
Sleep Mode is very useful for self voicing applications that have their
own screen reading functionality, or perhaps even some games that need
full use of the keyboard.

Although sleep mode can be toggled on and off by the user with the key
command NVDA+shift+s, a developer can choose to have sleep mode enabled
by default for an application. This is done by providing an App Module
for that application which simply sets sleepMode to True in the
AppModule class.

[]{#toc21}

### 3.12. Example 4: A Sleep Mode App Module

The following code can be copied and pasted in to a text file, then
saved in the appModules directory with the name of the application you
wish to enable sleep mode for. As always, the file must have a .py
extension.

    --- start ---
    import appModuleHandler

    class AppModule(appModuleHandler.AppModule):

        sleepMode = True

    --- end ---

[]{#toc22}

### 3.13. Providing Custom NVDA Object Classes

Providing custom NVDA Object classes is probably the most powerful and
useful way to improve the experience of an application in an NVDA
plugin. This method allows you to place all the needed logic for a
particular control altogether in one NVDA Object class for that control,
rather than scattering code for many controls across a plugin\'s events.

There are two steps to providing a custom NVDA Object class:

-   Define the NVDA Object class and its events, scripts, gesture
    bindings and overridden properties.
-   Tell NVDA to use this NVDA Object class in specific situations by
    handling it in the plugin\'s chooseNVDAObjectOverlayClasses method.

When defining a custom NVDAObject class, you have many NVDAObject base
classes to choose from. These base classes contain the base support for
the particular accessibility or OS API underlying the control, such as
win32, MSAA or Java access Bridge. You should usually inherit your
custom NVDAObject class from the highest base class you need in order to
choose your class in the first place. For example, if you choose to use
your custom NVDAObject class when the window class name is \"Edit\" and
the window control ID is 15, you should probably inherit from
NVDAObjects.window.Window, as clearly you are aware that this is a
Window object. Similarly, if you match on MSAA\'s accRole property, you
would probably need to inherit from NVDAObjects.IAccessible.IAccessible.
You should also consider what properties you are going to override on
the custom NVDA Object. For instance, if you are going to override an
IAccessible specific property, such as shouldAllowIAccessibleFocusEvent,
then you need to inherit from NVDAObjects.IAccessible.IAccessible.

the chooseNVDAObjectOverlayClasses method can be implemented on app
modules or global plugin classes. It takes 3 arguments:

1.  self: the app module or global plugin instance.
2.  obj: the NVDAObject for which classes are being chosen.
3.  clsList: a Python list of NVDAObject classes that will be used for
    obj.

Inside this method, you should decide which custom NVDA Object class(es)
(if any) this NVDA Object should use by checking its properties, etc. If
a custom class should be used, it must be inserted into the class list,
usually at the beginning. You can also remove classes chosen by NVDA
from the class list, although this is rarely required.

[]{#toc23}

### 3.14. Example 5: Command to Retrieve the Length of Text in an Edit Field Using a Custom NVDA Object

This app module for notepad provides a command to report the number of
characters in edit fields. You can activate it using NVDA+l. Notice that
the command is specific to edit fields; i.e. it only works while you are
focused in an edit field, rather than anywhere in the application.

The following code can be copied and pasted in to a text file, then
saved in the appModules directory with the name of notepad.py.

    --- start ---
    import appModuleHandler
    from NVDAObjects.IAccessible import IAccessible
    import controlTypes
    import ui

    class AppModule(appModuleHandler.AppModule):

        def chooseNVDAObjectOverlayClasses(self, obj, clsList):
            if obj.windowClassName == "Edit" and obj.role == controlTypes.ROLE_EDITABLETEXT:
                clsList.insert(0, EnhancedEditField)

    class EnhancedEditField(IAccessible):

        def script_reportLength(self, gesture):
            ui.message("%d" % len(self.value))

        __gestures = {
            "kb:NVDA+l": "reportLength",
        }

    --- end ---

[]{#toc24}

### 3.15. Making Small Changes to an NVDA Object in App Modules

Sometimes, you may wish to make only small changes to an NVDA Object in
an application, such as overriding its name or role. In these cases, you
don\'t need the full power of a custom NVDA Object class. To do this,
you can use the NVDAObject\_init event available only on App Modules.

The event\_NVDAObject\_init method takes two arguments:

1.  self: the AppModule instance.
2.  obj: the NVDAObject being initialized.

Inside this method, you can check whether this object is relevant and
then override properties accordingly.

[]{#toc25}

### 3.16. Example 6: Labelling the Notepad Edit Field Using event\_NVDAObject\_init

This app module for notepad makes NVDA report Notepad\'s main edit field
as having a name of \"content\". That is, when it receives focus, NVDA
will say \"Content edit\".

The following code can be copied and pasted in to a text file, then
saved in the appModules directory with the name of notepad.py.

    --- start ---
    import appModuleHandler
    from NVDAObjects.window import Window

    class AppModule(appModuleHandler.AppModule):

        def event_NVDAObject_init(self, obj):
            if isinstance(obj, Window) and obj.windowClassName == "Edit" and obj.windowControlID == 15:
                obj.name = "Content"
    --- end ---

[]{#toc26}

4. Packaging Code as NVDA Add-ons
---------------------------------

To make it easy for users to share and install plugins and drivers, they
can be packaged in to a single NVDA add-on package which the user can
then install into a copy of NVDA via the Add-ons Manager found under
Tools in the NVDA menu. Add-on packages are only supported in NVDA
2012.2 and later. An add-on package is simply a standard zip archive
with the file extension of nvda-addon which contains a manifest file,
optional install/uninstall code and one or more directories containing
plugins and/or drivers.

[]{#toc27}

### 4.1. Non-ASCII File Names in Zip Archives

If your add-on includes files which contain non-ASCII (non-English)
characters, you should create the zip archive such that it uses UTF-8
file names. This means that these files can be extracted properly on all
systems, regardless of the system\'s configured language. Unfortunately,
many zip archivers do not support this, including Windows Explorer.
Generally, it has to be explicitly enabled even in archivers that do
support it. [http://www.7-zip.org/](7-Zip) supports this, though it must
be enabled by specifying the \"cu=on\" method parameter.

[]{#toc28}

### 4.2. Manifest Files

Each add-on package must contain a manifest file named manifest.ini.
This must be a UTF-8 encoded text file. This manifest file contains key
= value pares declaring info such as the add-on\'s name, version and
description.

[]{#toc29}

#### 4.2.1. Available Fields

Although it is highly suggested that manifests contain all fields, the
fields marked as mandatory must be included. Otherwise, the add-on will
not install.

-   name: A short unique name for the add-on. This is used to
    differentiate add-ons internally and is not shown to the user.
    (Mandatory)
-   summary: The name of the add-on as shown to the user. (Mandatory)
-   version: The version of this add-on; e.g. 2.0. (Mandatory)
-   author: The author of this add-on, preferably in the form Full Name
    \<email address\>; e.g. Michael Curran \<<mick@kulgan.net>\>.
    (Mandatory)
-   description: A sentence or two describing what the add-on does.
-   url: A URL where this add-on, further info and upgrades can be
    found.
-   docFileName: The name of the main documentation file for this
    add-on; e.g. readme.html. See the [Add-on Documentation](#AddonDoc)
    section for more details.

[]{#toc30}

#### 4.2.2. An Example Manifest File

    --- start ---
    name = MyTestAddon
    summary = Cool Test Add-on
    version = 1.0
    description = An example add-on showing how to create add-ons!
    author = Michael Curran <mick@kulgan.net>
    url = http://www.nvda-project.org/wiki/Development
    --- end ---

[]{#toc31}

### 4.3. Plugins and Drivers

The following plugins and drivers can be included in an add-on:

-   App modules: Place them in an appModules directory in the archive.
-   Braille display drivers: Place them in a brailleDisplayDrivers
    directory in the archive.
-   Global plugins: Place them in a globalPlugins directory in the
    archive.
-   Synthesizer drivers: Place them in a synthDrivers directory in the
    archive.

[]{#toc32}

### 4.4. Optional install / Uninstall code

If you need to execute code as your add-on is being installed or
uninstalled from NVDA (e.g. to validate license information or to copy
files to a custom location), you can provide a Python file called
installTasks.py in the archive which contains special functions that
NVDA will call while installing or uninstalling your add-on. This file
should avoid loading any modules that are not absolutely necessary,
especially Python C extensions or dlls from your own add-on, as this
could cause later removal of the add-on to fail. However, if this does
happen, the add-on directory will be renamed and then deleted after the
next restart of NVDA. Finally, it should not depend on the existence or
state of other add-ons, as they may not be installed, have already been
removed or not yet be initialized.

[]{#toc33}

#### 4.4.1. the onInstall function

NVDA will look for and execute an onInstall function in installTasks.py
after it has finished extracting the add-on into NVDA. Note that
although the add-on will have been extracted at this time, its directory
will have a .pendingInstall suffix until NVDA is restarted, the
directory is renamed and the add-on is really loaded for the first time.
If this function raises an exception, the installation of the add-on
will fail and its directory will be cleaned up.

[]{#toc34}

#### 4.4.2. The onUninstall Function

NVDA will look for and execute an onUninstall function in
installTasks.py when NVDA is restarted after the user has chosen to
remove the add-on. After this function completes, the add-on\'s
directory will automatically be removed. As this happens on NVDA startup
before other components are initialized, this function cannot request
input from the user.

[]{#toc35}

### 4.5. Localizing Add-ons

It is possible to provide locale-specific information and messages for
your add-on. Locale information can be stored in a locale directory in
the archive. This directory should contain directories for each language
it supports, using the same language code format as the rest of NVDA;
e.g. en for English, fr\_CA for French Canadian.

[]{#toc36}

#### 4.5.1. Locale-specific Manifest Files

Each of these language directories can contain a locale-specific
manifest file called manifest.ini, which can contain a small subset of
the manifest fields for translation. These fields are summary and
description. All other fields will be ignored.

[]{#toc37}

#### 4.5.2. Locale-specific Messages

Each language directory can also contain gettext information, which is
the system used to translate the rest of NVDA\'s user interface and
reported messages. As with the rest of NVDA, an nvda.mo compiled gettext
database file should be placed in the LC\_MESSAGES directory within this
directory. to allow plugins in your add-on to access gettext message
information via calls to \_(), you must initialize translations at the
top of each Python module by calling addonHandler.initTranslation(). For
more information about gettext and NVDA translation in general, please
read <http://www.nvda-project.org/wiki/TranslatingNVDA>

[]{#AddonDoc}

### 4.6. Add-on Documentation

Documentation for an add-on should be placed in a doc directory in the
archive. Similar to the locale directory, this directory should contain
directories for each language in which documentation is available.

Users can access documentation for a particular add-on by opening the
Add-ons Manager, selecting the add-on and pressing the Add-on help
button. This will open the file named in the docFileName parameter of
the manifest. NVDA will search for this file in the appropriate language
directories. For example, if docFileName is set to readme.html and the
user is using English, NVDA will open doc\\en\\readme.html.

[]{#PythonConsole}

5. NVDA Python Console
----------------------

The NVDA Python console emulates the interactive Python interpreter from
within NVDA. It is a development tool which is useful for debugging,
general inspection of NVDA internals or inspection of the accessibility
hierarchy of an application.

[]{#toc40}

### 5.1. Usage

The console can be activated in two ways:

-   By pressing NVDA+control+z. If activated in this fashion, a snapshot
    of the current state of NVDA at the time the key was pressed will be
    taken and saved in certain variables available in the console. See
    [Snapshot Variables](#PythonConsoleSnapshotVariables) for more
    details.
-   By selecting Tools -\> Python console from the NVDA system tray
    menu.

The console is similar to the standard interactive Python interpreter.
Input is accepted one line at a time. The current line is processed when
enter is pressed. You can navigate through the history of previously
entered lines using the up and down arrow keys.

Output (responses from the interpreter) will be spoken when enter is
pressed. The f6 key toggles between the input and output controls.

Closing the console window simply hides it. This allows the user to
return to the session as it was left when it was closed, including
history and variables.

[]{#PythonConsoleNamespace}

### 5.2. Namespace

[]{#toc42}

#### 5.2.1. Automatic Imports

For convenience, the following modules and variables are automatically
imported in the console: sys, os, wx, log (from logHandler), api,
queueHandler, speech, braille

[]{#PythonConsoleSnapshotVariables}

#### 5.2.2. Snapshot Variables

Whenever NVDA+control+z is pressed, certain variables available in the
console will be assigned according to the current state of NVDA. These
variables are:

-   focus: The current focus object
-   focusAnc: The ancestors of the current focus object
-   fdl: Focus difference level; i.e. the level at which the ancestors
    for the current and previous focus differ
-   fg: The current foreground object
-   nav: The current navigator object
-   mouse: The current mouse object
-   brlRegions: The braille regions from the active braille buffer

[]{#toc44}

6. Remote Python Console
------------------------

A remote Python console is available for situations where remote
debugging of NVDA is useful. It is similar to the [local Python
console](#PythonConsole) discussed above, but is accessed via TCP.

Please be aware that this is a huge security risk. You should only
enable it if you are connected to trusted networks.

[]{#toc45}

### 6.1. Usage

To enable the remote Python console, use the local Python console to
import remotePythonConsole and call remotePythonConsole.initialize().
You can then connect to it via TCP port 6832.

History of previously entered lines is not supported.

The namespace is the same as [the namespace in the local Python
console](#PythonConsoleNamespace).

There are some special functions:

-   snap(): Takes a snapshot of the current state of NVDA and saves it
    in the [snapshot variables](#PythonConsoleSnapshotVariables).
-   rmSnap(): Removes all snapshot variables.