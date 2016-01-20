.. _type:

type
====

**Name**

``type - how it would be interpreted if used as a command name``

**Synopsis**

``type [option...] [name...]``

**Description**

For each name, indicate how it would be interpreted if used as a
command name.


-t 
    Type prints a single word which is one of \`alias', \`function',
    \`builtin', \`file' or \`keyword', if name is an alias, shell
    function, shell builtin, disk file, or shell reserved word,
    respectively.

-p 
    Type either returns the name of the disk file that would be
    executed, or nothing if \`-t' would not return \`file'.

-a 
    Type returns all of the places that contain an executable named
    file. This includes aliases and functions, if and only if the \`-p'
    option is not also used.


