.. _top:

top
===

**Name**

top -- display top CPU processes

**Synopsis**

**top** [option]

**Description**

top provides an ongoing look at processor activity in real time. It
displays a listing of the most CPU-intensive tasks on the system,
and can provide an interactive interface for manipulating
processes. It can sort the tasks by CPU usage, memory usage and
runtime.

Frequently used interactive commands

Several single-key commands are recognized while top is running.
Some are disabled if the s option has been given on the command
line.

-h 
    Displays a help screen giving a brief summary of commands, and the
    status of secure and cumulative modes.

-k 
    Kill a process.

-q 
    Quit.

-r 
    Re-nice a process. You will be prompted for the PID of the task,
    and the value to nice it to. Entering a positve value will cause a
    process to be niced to negative values, and lose priority.

-m 
    Toggle display of memory information.

-c 
    Toggle display of command name or full command line.

-p 
    Sort tasks by CPU usage (default).


