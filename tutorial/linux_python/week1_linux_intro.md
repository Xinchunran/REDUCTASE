Linux is a family of free and open-source operating systems based on the Linux kernel. Operating systems based on Linux are known as Linux distributions or distros. Examples include Debian, Ubuntu, Fedora, CentOS, Gentoo, Arch Linux, MACOS(Unix-like) and many others. 

"Read More: https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-basics"

In linux most of the 

```
/bin
/usr/bin
/sbin
```

First locate the file in your systems by using the "which". When you want to local your vim program on your systems

```
$ which vim
/usr/bin/vim
```

If you want to know where the program package located and the "which" command does not tell. Use "where" as an alternative. 

```
$ which which ##let's try to locate the 'which' program
which: shell built-in command
$ whereis which
```

### Accessing Directories
The following commands are useful for directory navigation:

|Command|Result|
|-------|-----------|
|cd 	|Change to your home directory|
|cd ..|Change to parent directory|
|cd - |Change to previous directory|
|cd /	|Changes your current directory to the root (/) directory|

### Exploring the Filesystem
The tree command is a good way to get a bird’s-eye view of the filesystem tree. The following commands can help in exploring the filesystem:

|Command|Result|
|-------|-----------|
|ls 	  |List the contents of the present working directory|
|ls –a  |List all files including hidden files and directories|
|tree   |Displays a tree view of the filesystem|
|tree -d|Just list the directories and suppress listing file names|


```
# ls -la file / ls -l file*
-rw-r--r-- 1 ranx yang_lab 703 Nov  4 23:55 files
```

The -i option prints out in the first column the i-node number, which is a unique quantity for each file object. This field is the same for both of the two files; what is really going on here is that it is only one file but it has more than one name associated with it,  as is indicated by the 2 that appears in the output.

```
# ln file1.txt file3.txt
# ls -li file*
134415251 -rw-r--r--. 3 root root 604 Feb 16 11:49 file1.txt
134415251 -rw-r--r--. 3 root root 604 Feb 16 11:49 file2.txt
134415251 -rw-r--r--. 3 root root 604 Feb 16 11:49 file3.txt
```
Changing the file3.txt means change the same object as named as file1.txt, file2.txt and file3.txt.

Symbolic or Soft links are created with the -s option as in:

```
# ln -s file1.txt file4.txt
# ls -li file*
134415251 -rw-r--r--. 3 root root 644 Feb 16 11:59 file1.txt
134415251 -rw-r--r--. 3 root root 644 Feb 16 11:59 file2.txt
134415251 -rw-r--r--. 3 root root 644 Feb 16 11:59 file3.txt
134415252 lrwxrwxrwx. 1 root root   9 Feb 16 11:59 file4.txt -> file1.txt
```
Notice file4.txt no longer appears to be a regular file, and it clearly points to file1 and has a different inode number. Symbolic links take no extra space on the filesystem. They are extremely convenient as they can easily be modified to point to different places. An easy way to create a shortcut from your home directory to long pathnames is to create a symbolic link.

Unlike hard links, soft links can point to objects even on different filesystems (or partitions) which may or may not be currently available or even exist. In the case where the link does not point to a currently available or existing object, you obtain a dangling link.

Hard links are very useful and they save space, but you have to be careful with their use, sometimes in subtle ways. For one thing if you remove either file1.txt or file2.txt in the example, the inode object will remain, which might be undesirable as it may lead to subtle errors later if you recreate a file of that name. If you edit one of the files, exactly what happens depends on your editor; most editors including vi and gedit will retain the link by default but it is possible that modifying one of the names may break the link and result in the creation of two objects.

**reference**
the majority of materials are obtaining from MinhKMA 

https://github.com/MinhKMA/Linux-Tutorial/blame/master/content/basic_commands.md
