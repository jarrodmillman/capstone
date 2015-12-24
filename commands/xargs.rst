.. _xargs:

xargs
=====

**Name**

xargs --  build and execute command lines from standard input

**Synopsis**

**xargs** [option...] [command] [initial-argument...]

**Description**

Execute COMMAND followed by its optionl INITIAL-ARGUMENTS and
append additional arguments found on standard input. Typically, the
additional arguments are filenames in quantities too large for a
single command line. **xargs** runs COMMAND multiple times to
exhaust all arguments on standard input.


-n MAXARGS 
    Limit the number of additional arguments to MAXARGS for each
    invocations of COMMAND.

-p 
    Interactive mode. Prompt the user for each execution of COMMAND.



