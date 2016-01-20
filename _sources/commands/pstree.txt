.. _pstree:

pstree
======

**Name**

pstree -- display a tree of processes

**Synopsis**

**pstree** [option]

**Description**

ps gives a snapshot of the current processes. If you want a
repetitive update of this status, use top.


-u 
    Show uid transitions. Whenever the uid of a process differs from
    the uid of its parent, the new uid is shown in parentheses after
    the process name.

-p 
    Show PIDs. PIDs are shown as decimal numbers in parentheses after
    each process name. -p implicitly disables compaction.



