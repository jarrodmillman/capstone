.. _grep:

grep
====

**Name**

``grep - print lines matching a pattern``

**Synopsis**

``grep [options] {pattern} [file...]``

**Description**

grep searches the named input *file* (or standard input if no files
are named, or the file name - is given) for lines containing a
match to the given *pattern*. By default, grep prints the matching
lines.

-c NUM, --context=NUM
    Print NUM lines of output context. Places a line containing --
    between contiguous groups of matches.

-h, --no-filename
    Suppress the prefixing of filenames on output when multiple files
    are searched.

-i, --ignore-case 
    Ignore case distinctions in both the *pattern* and the input
    files.

-n, --line-number
    Prefix each line of output with the line number within its input
    file.

-v, --invert-match
    Invert the sense of matching, to select non-matching lines.

