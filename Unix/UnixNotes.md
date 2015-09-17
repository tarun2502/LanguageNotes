### Common Questions
* If you need to run the command in your current directory then use ./fielName as current directory may not be in your path and bash will not know how to run the command.
### Prompt and Shells
* $ => Means you are logged in as a regular user.
* # => Means you are logged in as an administrator.
* tarun@machine:/tmp$ => Means user tarun is logged as a regular user on machine and currently at folder /tmp.
* echo $SHELL => Gives you which shell you are using.
* bash => To go to the bash shell if you are on another shell.
* exit or Ctrl + D=> To come out of the shell.
* Instruction to install bash shell on 1.4 of Learing Bash Shell Book.
* When login we start at the home directory created by administrator like /home/tarun. We can access the homedirectory using cd ~.
* Commands and their optiosn are case sensitive.
* Normal flow of commands.
  * Keyboard => Standard Input(Stdin) => Program => Standard Output(Stdout) => Terminal.
* By default all commands take input from standard input.
* Ctrl + D => To tell command that you are done with providing input.
  * Try this sort => followed by few words => Ctrl + D => It will sort the input.

* Ctrl + C => To stop a command, it sends a interrupt.


### File System
* There are three kind of files in Unix.
  * Normal Text files 
  * Executable files like shell scripts and programs.
  * Directories.
* The files do not require any extensions like windows. But we give extension as convention to recognise the files.

* Absolute path and Relative Path.
* Root use home directory is /root/ and all others are /home/name/
* /etc/ => Where configuration files live.
* /var/ => Its for variable files like tmp files which grow like system and application logs.
* /bin => Where executable binaries are stored for system.
* /sbin/ => Contains binaries to be used only by system administrators for system administration tasks.
* /lib/ => To support the binaries located around the system.
* /usr/ => Binaries for user programs.
### COMMANDS
* Every command is of the form "command -option argument
* Some commands will give you help if you do not provide arguments.

#### pwd
* It prints the current working directory.
* pwd -L => Its the same as pwd. It prints your logical path.
* pwd -P => It prints the physical path if you are using symlinks otherwise same as -L option.[TODO]Test this option when you understand symlinks.


#### cd 
* It means change directory.
* cd .. => Go to the parent of this directory.
* cd - => Go to the previous directory.
* cd => Go to your home directory.
* cd file => Get a error message

### mkdir
* mkdir notes => To make a directory notes.
* Can use relative or absolute path while creating directory.

### mv


### cp


### rmdir
* To remove a empty directory.
* If a directory has files in int you can't remove it by rmdir. Use rm in that case.

#### ls
* ls => Short name for list simply prints the file and directory  names in directory.
* ls -l => Prints the long information.To know what is long format do man ls => /Long Format
* ls -a => It includes directory entries whose name begin with .
* Long Format => file mode, number of links, owner name, group name, number of bytes in the file, last time file was modified, path name.

#### Regular expression
* For arguments to ls command we can provide regular expression.
  * ? Any singel character
  * * Any string of characters. Can match 0 character.
  * [set] Any character in set
  * [!set] Any character not in set
  * ls \*{jpg,JPG} matches both Jade.jpg, rose.JPG 
  * Above is a shortcut for ls \*jpg \*JPG

  


#### type
* To know where a particular program is located.
* It searches your environment(including aliases, keyword, functions, built-ins and $PATH.) for executable command matching its argument and prints the type and location of any matches.
* type python => where the python executable is located.
* type -a python => To search for all the places and not stop at the first match.


### which
* Its similar to type command but searches only in your $PATH and csh aliases.
* which -a python => Search for all the places python is located.


### apropos
* Searches manpages names and description for regular expressioin provided as arguments.
* Useful if you do not know the name of the command.
* apropos type
* Its similar to man -k RegularExpression


### locate


### slocate

### uptime


### host
* host udacity.com

### history
* prints out the whole history of commands.
* command can also be accessed by Ctrl + R

### unzip
* unzips the zip file.
* unzip filename => This will unzip the filename in current directory.

### cat 
* concatenate files 
* cat file1 file2 => it will concatenate and print the output.

### wc
* tells how many lines, words, bytes are there in a file.
* wc file1

### diff
* diff compares two files.

### rm
* rm -rf => remove all directories and subdirectories recursively and forcefully.


### ping
* To know if the other machine is alive.

### bc
* A simple calculator on the prompt.

### less
* test viewer.
* j, k => Normal down and up
* sapce bar => down one page
* u => up one page
* <, > => Go to start , Go to end.
* : line no => Go to the line number.
* You can use regular expression while searching.


### nano
* A simple editor availble in linux
* nano filename.

### LinksToRead
* http://askubuntu.com/questions/60218/how-to-add-a-directory-to-my-path
* http://sheet.shiar.nl/less
* http://codular.com/regex
