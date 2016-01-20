Shell Customization
===================

There will come a time when some modification of the shell
environment will be desired. Fortunately, in bash this is very
easily done.

**Table C-1. Bash Configuration File**

=====================   =========================
File                    Description
=====================   =========================
``/etc/profile``        System login environment
``/etc/bashrc``         System environment
``~/. bash\_profile``   User login environment
``~/. bashrc``          User environment
``~/. bash\_logout``    User logout script
=====================   =========================

If no ``.bash_profile``, then ``.bash_login``, then ``.profile``.  


**Table C-2. Prompt String Customization**


========  =========================================================
Command   Meaning
========  =========================================================
``\d``    The date in "Weekday Month Day" format
``\H``    The hostname
``\h``    The hostname up to the firlst "."
``\n``    A carriage return and line feed
``\T``    The current time in 12-hour HH:MM:SS format
``\t``    The current time in HH:MM:SS format
``\@``    The current time in 12-hour am/pm format
``\u``    The username of the current user
``\w``    The current working directory
``\W``    The basename of the current working directory
``\#``    The command number of the current command
``\!``    The history number of the current command
``\$``    If the effective UID is 0 print a #, otherwise print a $
``\\``    Print a backslash
========  =========================================================
