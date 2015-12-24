.. _ln:

ln
==

**Name**

ln -- make links between files

**Synopsis**

**ln** [options...] {target...} [link\_name]

**Description**

Create a link to the specified TARGET with optional LINK\_NAME. If
LINK\_NAME is omitted, a link with the same basename as the TARGET
is created in the current directory. When using the second form
with more than one TARGET, the last argument must be a directory;
create links in DIRECTORY to each TARGET. Create hard links by
default, symbolic links with --symbolic. When creating hard links,
each TARGET must exist.


-i, --interactive
    prompt whether to remove destinations

-f, --force
    remove existing destination files

-s, --symbolic
    make symbolic links instead of hard links


