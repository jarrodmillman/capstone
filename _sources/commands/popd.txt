.. _popd:

popd
====

**Name**

``popd -  remove the top entry from the directory stack, and cd to
the new top directory``

**Synopsis**

``popd [option...]``

**Description**

Remove the top entry from the directory stack, and cd to the new
top directory. When no arguments are given, popd removes the top
directory from the stack and performs a cd to the new top
directory.

- +N 
    Removes the Nth directory (counting from the left of the list
    printed by dirs), starting with zero.

- -N 
    Removes the Nth directory (counting from the right of the list
    printed by dirs), starting with zero.



