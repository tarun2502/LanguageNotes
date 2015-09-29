### package installation 
* All your package sources are stored in /etc/apt/sources.apt
* cat /etc/apt/sources.apt
* To update package source list => sudo apt-get update
* To update the packages on our system => sudo apt-get upgrade
* man apt-get  => use this to get more information about apt-get
* To install software => sudo apt-get install packagename
* To search for packages => packages.ubuntu.com and search there.


### User Details
* All user details are stored in file /etc/passwd.
* Its of the form username:encryptedPass(these days unix distribution insert just a character x to ignore this field as encrypted passwd can be cracked.):userid:groupid:User description(may be empty):User's home directory: User's default shell


### Add a user
* `sudo adduser student` meaning add a use named student.
 
### Generating ssh key
* 'ssh-keygen' => Generating pair of private/public key.


### File Permissions.
* Filettype[- or d]|owner|group|everyone(rwx)
* r = 4, w = 2, x = 1 none = 0

### chmod 
* Change file permissions.

### chgrp
* Change group of the file or directory.
* `sudo chgrp root .bash_history`=> will change the group to root.

### chown
* Change the owner of file
* `sudo chwon root .bash_history` => will change the owner of .bash_history to root.

### Ports
* How does a application know how to respond to a request.
* Each application is configured to respond to a request on a port.
* Common Ports => Http=80, Https = 443, Ftp=20-21,SSh=22, Pop3=110, Smtp=25 
* [CommonPorts](http://bandwidthcontroller.com/applicationPorts.html)


### Firewall
* Ubuntu comes with a firewall installed
* `sudo ufw status` => To know the status of firewall.
* `sudo ufw default deny incoming` =>Initially block everything then only allow what your need. => Rule of least privileage.
* `sudo ufw default allow outgoing` => Allow all outgoing request.
* `sudo ufw allow ssh` => To allow all incoming ssh request.
* `sudo ufw allow 2222/tcp` => Because we are on a virtual machine we are allowing all tcp connections on port 2222.
* `sudo ufw allow www` => we allow a http server on port 80
* `sudo ufw enable` => Enable the firewall.
* `sudo ufw status` => To get the status.
