.. _wget:

wget
====

**Name**

wget -- GNU Wget Manual

**Synopsis**

**wget** [option...] [URL...]

**Description**

GNU Wget is a free utility for non-interactive download of files
from the Web. It supports HTTP, HTTPS, and FTP protocols, as well
as retrieval through HTTP proxies.

Frequently used download options

-nc, --no-clobber 
    If a file is downloaded more than once in the same directory,
    Wget's behavior depends on a few options, including -nc. In certain
    cases, the local file will be clobbered, or overwritten, upon
    repeated download. In other cases it will be preserved.

-c, --continue 
    Continue getting a partially-downloaded file. This is useful when
    you want to finish up a download started by a previous instance of
    Wget, or by another program.


Frequently used directory options

-nd, --no-directories 
    Do not create a hierarchy of directories when retrieving
    recursively.


Frequently used HTTP options
 
    


Frequently used FTP options

-g on/off, --glob=on/off 
    Turn FTP globbing on or off. Globbing means you may use the
    shell-like special characters (wildcards), like \*, ?, [ and ] to
    retrieve more than one file from the same directory at once.

-passive-ftp 
    Use the passive FTP retrieval scheme, in which the client initiates
    the data connection.

-retr-symlinks 
    When --retr-symlinks is specified, however, symbolic links are
    traversed and the pointed-to files are retrieved.


Frequently used recursive retrieval options

-r, --recursive 
    Turn on recursive retrieving.

-l DEPTH, --level=DEPTH 
    Specify recursion maximum depth level DEPTH.

-k, --convert-links 
    After the download is complete, convert the links in the document
    to make them suitable for local viewing.



