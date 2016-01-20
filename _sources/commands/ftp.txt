.. _ftp:

ftp
===

**Name**

``ftp - ARPANET file transfer program``

**Synopsis**

``ftp [option]``

**Description**

FTP is the user interface to the ARPANET standard File Transfer
Protocol. The program allows a user to transfer files to and from a
remote network site.

**Frequently used options**

-i 
    Turns off interactive prompting during multiple file transfers.

**Frequently used commands**

The client host with which ftp is to communicate may be specified
on the command line. If this is done, ftp will immediately
attempt to establish a connection to an FTP server on that host;
otherwise, ftp will enter its command interpreter and await
instructions from the user. When ftp is awaiting commands from
the user the prompt \`\`ftp>'' is provided to the user. The
following commands are recognized by ftp:

-cd REMOTE-DIRECTORY 
    Change the working directory on the remote machine to
    REMOTE-DIRECTORY.

-delete REMOTE-FILE 
    Delete the file REMOTE-FILE on the remote machine.

-get REMOTE-FILE [LOCAL-FILE] 
    Retrieve the file remote-file and store it on the local machine.

-glob 
    Toggle filename expansion for mdelete, mget, and mput.

-hash 
    Toggle hash-sign (\`\`#'') printing for each data block
    transferred. The size of a data block is 1024 bytes.

-ls [REMOTE-DIRECTORY] [LOCAL-FILE]
    Print a listing of the contents of a directory on the remote
    machine.

-mdelete [REMOTE-FILES]
    Delete REMOTE-FILES on the remote machine.

-mget REMOTE-FILES
    Expand the REMOTE-FILES on the remote machine and do a get for each
    file name thus produced.

-mput LOCAL-FILES
    Expand the REMOTE-FILES on the remote machine and do a get for each
    file name thus produced.

-passive
    Toggle passive data transfer mode off.

-prompt
    Toggle interactive prompting.

-put LOCAL-FILE [REMOTE-FILE]
    Store a local file on the remote machine.

-pwd
    Print the name of the current working directory on the remote
    machine.

-quit
    A synonym for bye.


