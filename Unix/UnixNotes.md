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
* set -x sets the debug level on the commmand line.
* Commands and their optiosn are case sensitive.
* Shell first intrepets the command line and then runs the commmand.
* Normal flow of commands.
  * Keyboard => Standard Input(Stdin) => Program => Standard Output(Stdout) => Terminal.
* By default all commands take input from standard input.
* By default each program that starts up has all three I/O channels set to your terminal so standard I/O is your keyboard, and standard output and standard error is your terminal screen.
* we can also redirect so a program can read input from some file and provide output to some file or program.
* To redirect input use < . For e.g. cat < file will display the contents of file rather then taking input from user.
* To redirect output use > . For e.g. "time > now" will redirect output of command time to a file name as now. It will not show on screen.
* A nice trick => cp file1 file2 => cat < file1 > file2
* To redirect output of one command to input of another use pipeline | . e.g "sort < file1 | more" 
  * Another e.g. "cut -d: -f1 < /etc/passwd | sort" => To read the file /et/passwd which is delimited by : and get its first column and sort it. 
  * Pipeline eliminates the need to store data in temporary files. 
* Ctrl + D => To tell command that you are done with providing input.
  * Try this sort => followed by few words => Ctrl + D => It will sort the input.

* ^ + m = RETURN key
* To see your setting => stty all
* Ctrl + C => To stop a command, it sends a interrupt.

### Running background job => Just add the & at the end of command.
  * uncompress gcc.tar & 
  * You can check the status of background jobs using command jobs  which prints the job status.
  * Ideally program requiring input and output should be done to a file so that current shell prompt is not disturbed.
  * $ diff a.txt a_old.txt > diffresult.txt &
  * Every job is assigned a priority and based on that priority its allocated system resources.
  * System admin can increase or decrease priority.
  * "nice" command can be used to run jobs at lower priority.

### Quoting => To use special characters literally i.e. witout their meaning.
  * echo 2 * 3 > 5 is a valid inequality => this will create a file containing 2, names of all files in our current dir and 3. Because shell expanded * to include all file in current directory.
  * 'echo 2 * 3 > 5 is a vaid inequality' => It will print the result as it is. Similarly echo '2 * 3 > 5' is a valid inequlity as you do not need to escape the whole command only the part containing special characters.
  * Another way to esccape is using \. echo 2 \* 3 \> 5 is a valid inequality will print it literally. To quote a \ use \\ or '\'
  * find . -name '\*.c' => Here we need to escape it otherwise shell will expand it to include it in current file name.
  * echo \"2 \* 3 \> 5 \" is a valid inequality will print => "2 * 3 > 5 " is a valid inequality.
  * Continuing lines => You need to quote the RETURN key. Use \ or not closing '(by including return in quoted string) to do it.Note that after \ there should be only return key and nothing else.  
* Shell responds with > secondary prompt and waits for you to finish the command.
* Using double quotes => echo "$USER won't pay \$5 for coffee." => Tarun won't pay $5 for coffee. => we escape $ because otherwise shell evaluates it.
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

# Users
* In every unix system, user root is availbale by default. So first thing remove remote access to root user so that a hacker can not access.

### COMMANDS
* Every command is of the form "command -option argument
* Some commands will give you help if you do not provide arguments.

### sudo
* To run the current command as super user.
* sudo ls -al /home/ubuntu/.ssh
* This is recommended as if you directly go to super user mode and start running commands than you may forget that you are in super user mode and incidently run some harmful commands.
* So it's recommmended to use sudo for running some commands as super user.
* Not every user can run commands as super user. You have to give him special permissions to run sudo command.	

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
* cd . => Remain in current directory => cd .\a.html => Just to show that we are in current directory.

### mkdir
* mkdir notes => To make a directory notes.
* Can use relative or absolute path while creating directory.

### mv


### cp


### rmdir
* To remove a empty directory.
* If a directory has files in int you can't remove it by rmdir. Use rm in that case.

#### ls
* ls => Short name for list simply prints the file and directory  names in directory. By default the order is arranged alphabetically with upercase having precedece over lowercase (we call ASCII collating sequence)
* ls -l => Prints the long information.To know what is long format do man ls => /Long Format
* ls -a => It includes directory entries whose name begin with . To show all files.
* ls -r => Reverse the default sorting order.
* ls -t => Sort by modification time, newest first.
* Long Format => file mode, number of links, owner name, group name, number of bytes in the file, last time file was modified, path name.

#### Regular expression
* For arguments to ls command we can provide regular expression.
* Our commands only see the result of wildcard expansion. For e.g in a directory with files fred and frank if you type ls fr\* then ls command will see it as "ls fred frank" and print the output. If you type "ls g\*" then it will see it as "ls g\*" only as there are no files with that name and print error as "no such files or directory"
* They can be used in path name expansion also. For e.g. "ls /usr/\* " will list file in both directory /usr1 and /usr2
  * ? Any single character
    * program.? matches => program.c, program.o but not program.log
  * * Any string of characters. Can match 0 character.
    * program.\* can match program.c, program.o and program.log
    * If shell can't match anything it jsut leaves the string with wildcard untouched.
  * [set] Any character in set
    * program.[co] and program.[a-z] both match program.c and program.o but not program.log
  * [!set] Any character not in set
	* [!a-zA-Z] matches any characterthat is not alphabet.
    * To match ! place it after first character or \!

  * ls \*{jpg,JPG} matches both Jade.jpg, rose.JPG 
  * Above is a shortcut for ls \*jpg \*JPG
  * echo b{ed,olt,ar}s matches beds, bolts, bars. We can nest also.

  


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
* Shows the uptime of system, no of users logged in, load average.
* Load Average => 1 min, 5 min, 15 min average of how really system the busy is.

### hostname
* shows name of your machine.

### host
* host udacity.com

### uname
* The name of operating system.
* `uname -a` => All the info you need.

### ps 
* To know the runnig processes.
* -f => formatting options.
* -u => to know the process run by a user => `ps -fu tarunsharma`
* formatting options
  * UID = user id who started the processes.
  * PID = Process id
  * PPID = Parent Process Id => Parent who started this processes. May be init processes the first processes starts when linux booted up.
  * C = CPU being used.
  * STIME = At what time the processes starts.
  * TTY = what terminal is attached to processes.
  * TIME = How much cpu time this processes has used.
  * CMD = what's the command being run.
* -e = show me everything running on this system. `ps -ef`
* `ps aux` => Berkely version of ps -ef => To know its format use `ps u`
* ps aux formats.
  * User = user 
  * PID = Processes id
  * %CPU = %CPU being used.
  * %Mem = % memory being used.
  * VSZ = Virtual size => memory allocated to program , program thinks that it has this memeory.
  * RSS = Resident Size => Actual memory being used by program.
  * STAT =Current Process status ; S => Process is sleeping.; R => Process is running.

### kill
* To kill the running processes.
* kill processId
* Zombie Processes => Process started and then abandoned by parent.
* To kill a zombie process kill parent.
### top
* Gives constantly updating status of your system memory and processes.
* `top` ; type q to quit. 
### history
* prints out the whole history of commands.
* command can also be accessed by Ctrl + R

### unzip
* unzips the zip file.
* unzip filename => This will unzip the filename in current directory.

### who
* display who are current users logged into the system.
### cat 
* concatenate files 
* cat file1 file2 => it will concatenate and print the output.

### head
* To see the top of any input
* By default top 10 lines
* `can control by head -5 abc.txt` => only 5 lines
* `head -5 abc.txt def.txt` => will show the 5 lines of both the files.

### tail
* To see the tail of any input
* By default shows the last 10 lines.
* Can control output => `tail -5 abc.txt` => Show only last 5 lines.
### wc
* tells how many lines, words, bytes are there in a file.
* `wc file1`
* `ls|wc -l` => To know how many files are there in current dir.

### diff
* diff compares two files.

### rm
* rm -rf => remove all directories and subdirectories recursively and forcefully.


### ping
* To know if the other machine is alive.

### bc
* A simple calculator on the prompt.

### cal 
* Calendar.
* `cal` => To display current month calender.
* `cal 7 2006` => To display for July 2006

### less
* file viewer, shows start of file and then stops.
* j, k => Normal down and up
* sapce bar => down one page, b => back one space
* u => up one page
* <, > => Go to start , Go to end.
* : line no => Go to the line number.
* You can use regular expression while searching.
* less +F filename => tail kind of functionality.
* h for help.
* q for quitting the file
* `less file1 file2` => Shows first file and then type :n go to the next file.


### df
* To get the disk free
* By default shows disk space in blocks format 
* -h => `df -h` => Shows in human readable format.

### nano
* A simple editor availble in linux
* nano filename.

### stty
* Your system key settings.
* type "stty all" to know your system settings.

### help
* Provides help on some commands.
* help cd 

### tput
* To clear screen.
* `tput clear`

### LinksToRead
* http://askubuntu.com/questions/60218/how-to-add-a-directory-to-my-path
* http://sheet.shiar.nl/less
* http://codular.com/regex

