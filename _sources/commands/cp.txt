.. _cp:

cp
==

**Name**

``cp - copy files and directories``

**Synopsis**

``cp [options...] {source...} {dest}``

**Description**

Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.

-a, --archive
    same as -dpR

-d 
    same as --no-dereference --preserve=link

-p
    same as --preserve=mode,ownership,timestamps

-r 
    copy recursively, non-directories as files WARNING: use -R instead
    when you might copy special files like FIFOs or /dev/zero

-i, --interactive
    prompt before overwrite

-R, --recursive
    copy directories recursively


