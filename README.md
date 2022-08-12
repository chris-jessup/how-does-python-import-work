# how-does-python-import-work
How Does Python Import Work?

## What is the Purpose of modules?

The two primary purposes are organisational and information hiding. Python by default does not hide information.

## Python's Imports are magical

Unlike many other languages, you can run arbitrary code at import time in Python.

This allows many useful things, like setting up connections to external services,
but the lack of direct control over execution is .... spooky.

## What is the purpose of '__init__.py'?

The '__init__.py' file, even if empty, tells the python interpreter that the currnt
folder is a module.

You can even define your whole module inside '__init__.py' (see potter/teachers/__init__.py)

## How to inspect a module?

There are two primary ways to inspect a module - using 'dir(<module_name>)' or 'help(<module_name>)'.

There are many other tools

## How to hide information in a module?

There are 3 primary ways:

* By convention. Prepending an underscore to a name tells the user that that object is internal
* By import. In __init__.py you can directly import what you want to expose and leave out what you don't
* By using __all__. __all__ is very magical but seems to be able to specify exactly what gets exported. I couldn't get it to work
