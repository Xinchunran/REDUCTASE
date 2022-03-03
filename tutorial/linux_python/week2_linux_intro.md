##Introduction
The shell command is quite useful tool in dealing with bioinfomatics problems saying sequence files proceeding, aligement of the protein sequneces etc. Also in most of the HPC workspace the bash is quite import to connect the files from different data folders.         

The **shell** is a command line interpreter which provides the user interface for terminal windows. It can also be used to run scripts, even in non-interactive sessions without a terminal window, as if the commands were being directly typed in.        


##More cheat sheet
https://devhints.io/bash


```
#!/bin/bash
find /usr/lib -name "*.so" -ls

'''A . so file is a "shared object", or library file containing compiled code that can be linked to a program at run-time. It is the Linux equivalent of a Windows DLL (dynamic link library).'''

```
The first line of the script, that starts with ``#!/bin/bash`` contains the full path of the command interpreter that is to be used on the file. The command interpreter is tasked with executing statements that follow it in the script. Commonly used interpreters include:

```
/usr/bin/perl
/bin/bash
/bin/csh
/bin/tcsh
/bin/ksh
/usr/bin/python
/bin/sh
```

Scripting is not only limited to shell interpreter. It can be used for Python scripts too.
```
# ll week2_linux_script
# cat script
#!/usr/bin/python
# ./script
Welcome to the Python script
```

Scripts can be interactive too.

the tutorial is obtained from https://github.com/MinhKMA/Linux-Tutorial
