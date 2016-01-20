.. _pushd:

pushd
=====

**Name**

``pushd - save the current directory on the top of the directory
stack and then cd to dir``

**Synopsis**

``pushd [option...]``

**Description**

Save the current directory on the top of the directory stack and
then cd to dir. With no arguments, pushd exchanges the top two
directories.

- +N 
    Brings the Nth directory (counting from the left of the list
    printed by dirs, starting with zero) to the top of the list by
    rotating the stack.

- -N 
    Brings the Nth directory (counting from the right of the list
    printed by dirs, starting with zero) to the top of the list by
    rotating the stack.

-dir 
    Makes the current working directory be the top of the stack, and
    then executes the equivalent of \`cd dir'. cds to dir.


