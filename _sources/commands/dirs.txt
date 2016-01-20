.. _dirs:

dirs
====

**Name**

``dirs - display the list of currently remembered directories``

**Synopsis**

``dirs [options...]``

**Description**

Display the list of currently remembered directories. Directories
are added to the list with the pushd command; the popd command
removes directories from the list.


- +N 
    Displays the Nth directory (counting from the left of the list
    printed by dirs when invoked without options), starting with zero.

- -N 
    Displays the Nth directory (counting from the right of the list
    printed by dirs when invoked without options), starting with zero.

-c 
    Clears the directory stack by deleting all of the elements.

-l
    Produces a longer listing; the default listing format uses a tilde
    to denote the home directory.

-p 
    Causes dirs to print the directory stack with one entry per line.

-v
    Causes dirs to print the directory stack with one entry per line,
    prefixing each entry with its index in the stack.
