.. _find:

find
====

**Name**

``find - search for files in a directory hierarchy``

**Synopsis**

``find [path...] [expression]``

**Description**

find searches the directory tree rooted at each given file name by
evaluating the given expression from left to right, according to
the rules of precedence (see section OPERATORS), until the outcome
is known (the left hand side is false for and operations, true for
or), at which point find moves on to the next file name.

**Expressions**

The expression is made up of options (which affect overall
operation rather than the processing of a specific file, and always
return true), tests (which return a true or false value), and
actions (which have side effects and return a true or false value),
all separated by operators. -and is assumed where the operator is
omitted. If the expression contains no actions other than -prune,
-print is performed on all files for which the expression is true.

**Frequently used options**

It is best to place options at the beginning of the expression.

-mindepth levels 
    Do not apply any tests or actions at levels less than levels (a
    non-negative integer).

-maxdepth levels 
    Descend at most levels (a non-negative integer) levels of
    directories below the command line arguments.

-follow 
    Dereference symbolic links. Implies -noleaf.

**Frequently used tests**

Numeric arguments can be specified as:

+n
    for greater than n

-n
    for less than n

n
    for exactly n

-type c 
    File is of type c::

           b      block (buffered) special
           c      character (unbuffered) special
           d      directory
           p      named pipe (FIFO)
           f      regular file
           l      symbolic link 

-name pattern
    Base of file name (the path with the leading directories removed)
    matches shell pattern pattern.

-atime n
    File was last accessed n\*24 hours ago.

-amin n
    File was last accessed n minutes ago.

-anewer file
    File was last accessed more recently than file was modified.

-ctime n
    File's status was last changed n\*24 hours ago.

-cmin n
    File's status was last changed n minutes ago.


**Frequently used actions**

-print
    print the full file name on the standard output, followed by a
    newline.

-ls
    list current file in \`ls -dils' format on standard output.

-exec command
    Execute command; true if 0 status is returned. All following
    arguments to find are taken to be arguments to the command until an
    argument consisting of \`;' is encountered.

-ok command
    Like -exec but ask the user first

