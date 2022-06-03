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

```
cat script.sh
bash week2_interactive_bash
```

All shell scripts generate a return value upon finishing execution. The value can be set with the exit statement. Return values permit a process to monitor the exit state of another process often in a parent-child relationship. This helps to determine how this process terminated and take any appropriate steps necessary, contingent on success or failure. By convention, success is returned as 0, and failure is returned as a non-zero value. The return value is always stored in the $? environment variable.

|Character|Description|
|---------|-----------|
|#|Used to add a comment, except when used as \#, or as #! when starting a script|
|\\|Used at the end of a line to indicate continuation on to the next line|
|;|Used to interpret what follows as a new command|
|$|Indicates what follows is a variable|

Sometimes you may want to group multiple commands on a single line. The semicolon character is used to separate these commands and execute them sequentially as if they had been typed on separate lines.


### Functions
A function is a code block that implements a set of operations. Functions are useful for executing procedures multiple times perhaps with varying input variables. Functions are also often called subroutines. Using functions in scripts requires two steps:

1. Declaring a function
2. Calling a function

The function declaration requires a name which is used to invoke it. The proper syntax is:
```
    function_name () {
	           command...
	}
```

For example, the following function is named display:

```
    display(){
	echo "this is a sample function"    
    }

```

The function can be as long as desired and have many statements. Once defined, the function can be called later as many times as necessary. In the full example shown in the figure, we are also showing an often-used refinement: how to pass an argument to the function.  The first, second, ..., n-th argument can be referred to as ``$1, $2, ..., $n``. The script name is referred as ``$0``. All parameters are referred as ``$*`` and the total number of arguments is ``$#``.

### Command substitution
You may need to substitute the result of a command as a portion of another command. It can be done in two ways:

1. By enclosing the inner command with backticks (`)
2. By enclosing the inner command in $( )
No matter the method, the innermost command will be executed in a newly launched shell environment, and the standard output of the shell will be inserted where the command substitution was done. Virtually any command can be executed this way. Both of these methods enable command substitution; however, the second method allows command nesting.
```
# cat ./count.sh
# ./count.sh /var/log/messages
The  /var/log/messages  contains  114  lines.
0
```

the tutorial is obtained from https://github.com/MinhKMA/Linux-Tutorial
