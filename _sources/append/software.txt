*********************
Software installation
*********************

.. contents::

Text editor
===========

You will need an editor for text to edit code and other things.

Your text editor will be your constant companion and you should chose
carefully.

Your teachers use the ``vim`` text editor; this is very powerful but has
a steep learning curve. The editors we recommend below are easier to use
without practice, but less powerful.

Windows
-------

We suggest `Notepad++ <http://notepad-plus-plus.org>`__.

Go to the "Download" page; download and run the ``.exe`` installer.

In BASH

.. code:: bash

    $ export PATH=/c/Program\ Files/Notepad++:$PATH
    $ alias edit='notepad++'

OSX
---

We suggest
`TextWrangler <http://www.barebones.com/products/textwrangler>`__.
Download the ``.dmg`` installer. Run the file to get the disk icon on
the desktop like this:

.. figure:: ../figs/tw_dmg.png
   :alt: TextWrangler DMG

   TextWrangler DMG

Double click the disk icon to get something like this:

.. figure:: ../figs/tw_install.png
   :alt: TextWrangler install

   TextWrangler install

Drag the TextWrangler icon to the Applications folder icon to install.

Open TextWrangler by going to your Applications folder and
double-clicking the TextWrangler icon.

Go to the TextWrangler menu and make sure you have installed the command
line tools:

.. figure:: ../figs/tw_command_line.png
   :alt: TextWrangler command line

   TextWrangler command line

Git setup
=========

`git <http://git-scm.com>`__ is the standard version control software
that allows us to keep a record of changes and to share changes with
other people.

Windows
-------

Follow the instructions
`here <http://git-scm.com/book/en/Getting-Started-Installing-Git#Installing-on-Windows>`__.

If you installed Notepad++ you will need to tell git to use Notepad++ as
your editor when git needs text descriptions.

First open windows explorer to check where Notepad++ got installed. The
program may be in ``C:/Program Files/Notepad++/notepad++.exe`` or in
``C:/Program Files (x86)/Notepad++/notepad++.exe``. Check which.

Then double click the git bash icon:

.. figure:: ../figs/git_bash_icon.png
   :alt: git bash icon

   git bash icon

From this web page, select and copy the command that matches where your
Notepad++ was installed::

    $ git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

or ::

    $ git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

Select the top left corner of the git bash window to get the window
menu, then find the 'Edit' menu 'Paste' option to paste the command into
git bash:

.. figure:: ../figs/git_bash_paste.png
   :alt: git bash paste

   git bash paste

When you've pasted, press return:

.. figure:: ../figs/git_bash_configged.png
   :alt: git bash configged

   git bash configged

(These instructions are from
`stackoverflow <http://stackoverflow.com/questions/1634161/how-do-i-use-notepad-or-other-with-msysgit/2486342#2486342>`__)

You can check that your editor is properly configured by typing::

   $ git config --global -e

in the git bash window. It should fire up Notepad++ with a text file
with some settings for git. Don't change anything, close the file.

OSX
---

Download and run the installer for `git on
OSX <http://code.google.com/p/git-osx-installer>`__.

If you installed TextWrangler you need to tell git to use it as your
text editor.

-  make sure you installed the TextWrangler command line tools (see
   above).
-  Open ``Terminal`` (Command key and space, type 'Terminal' to find the
   Terminal app)
-  At the Terminal command line, type:

   ``$ git config --global core.editor "edit -w"``

(These instructions are from
`stackoverflow <http://stackoverflow.com/questions/13257519/how-to-change-the-default-editor-for-git>`__)

You can check your editor is properly configure by typing::

    $ git config --global -e

in the Terminal window. It should fire up TextWranger with a text file
with some settings for git. Don't change anything, close the file.
