# t1w7-python-mod-pack

## Wildcard Arguments
- When you don't know how many arguments to pass in a function.
- Non-keyword argument: *args [code](math_ops.py)
- Keyword argument: **kwargs [code](kwarga_eg.py)

## Modules
[code](using_modules.py)
- One of the techniques for following DRY Coding Principles.
- Group similar codes and functions together is seperate files.
- Solves the problem of code file being too lengthy and complex.
- Can be reused accross several programs.
- Python comes with a lot of modules as well, Pythons Standard Library.

## Packages
[package](maths_package) [using_package](using_package.py)
- Collections of modules
- Organise related modules under one directory
- Initialise a package using __init__.py file

### Practicle Example 
[code](text_processing)
Task:
- Create a package for basic text processing with modules for:
    - Counting words in a string
    - Counting characters in a string
    - Reversing strings

## Slicing a sequence
[slicing code](slicing.py)
- A way to extract part of data structures, like strings, lists, tuples etc.
- Syntax: sequence[start:stop:step] (like range)
- Defaukt of start: 0, Default of step: 1, stop: last

## Object Oriented Programming
- It is a way to help programmers structure the  functionality of your program that would make sense to humans and allow computers to run it efficiently