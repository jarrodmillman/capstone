File Transfer
=============

Interactive
------------

To interactively copy a few files between machines the
following commands are often sufficient.

**ftp** and **sftp**
~~~~~~~~~~~~~~~~~~~~

Useful Contents

* :ref:`ftp` -- ARPANET file transfer program
* :ref:`sftp` -- Secure file transfer program

**scp** and **wget**
~~~~~~~~~~~~~~~~~~~~

Useful Contents

* :ref:`scp` -- secure copy
* :ref:`wget`-- GNU Wget Manual

However, if you need to transfer a substantial amount
of data between machines, the weakness of these commands
(`sftp`, `scp`, and `wget`)
become apparent.


SSH Tar pipe
------------

For one-time bulk transfer of data, the best solution is to
use a ssh tar pipe.  Basically the idea is to pipe together
two tar commands with a ssh pipe.  One of the tar commands
streams the files to be tranferred to stdout and the other
tar command unpacks the files from stdin. 

Here are the two main ways I use this technique to transfer files.
You can either transfer files from the machine you are on to a remote
machine or you can transfer files from a remote machine to the one you
are on.

#.  When I want to transfer data from the machine I am on to a
    remote host.  More specifically, imagine that I am logged in
    as 'user1' on a machine named 'local'.  In my home directory,
    I have a big data directory or file called 'something' that
    I want to copy onto a remote machine named 'remote' into
    some path '/somewhere'. I could do this via the following
    command::

      [user1@local ~]$ tar cf - something | ssh remote " ( cd /somewhere ; tar xf - ) "

    This command doesn't give you any output, which can be very
    frustrating when transferring a lot of data.  So I recommend adding
    the verbose flag '-v' to the second tar command::

      [user1@local ~]$ tar cf - something | ssh remote " ( cd /somewhere ; tar xvf - ) "

    Also, if this is going to take a long time you may want to use a
    screen session.

#.  When I want to transfer data from a remote host to the machine I am on.

    ::

      ssh remote "( cd /somewhere ; tar cf - something ) " | tar xf -

Using rsync to mirror remote directories
----------------------------------------

If you want to mirror some data, then rsync is a better solution than
a ssh tar pipe.  However, you may want to use a ssh tar pipe to initially
transfer the the data in bulk and then use rsync to keep the two data sets
in sync.

What is rsync?
~~~~~~~~~~~~~~

``rsync`` is a fast, powerful, and configurable file transfer tool.  In
particular, ``rsync`` is widely used due to its ability to only transfer
the differences between files at the source and existing files at the
destination.  It has a large number of options, which allow you to control
nearly every aspect of its operation.  Given its extreme versitality there
are numerous online tutorials describing how to use it in a large variety
of ways.  In particular, please take a look at the following:

* `rsync man page <http://www.samba.org/ftp/rsync/rsync.html>`__
* `rsync Tips & Tricks <http://sial.org/howto/rsync/>`__


For this tutorial, we will just be discussing mirroring files between
two UNIX systems. We will also only discuss using rsync with a remote
shell.  So, if you want to:

* mirror between two systems with different file permission models
* are interested in setting up or using the ``rsync`` daemon

you may need to refer to the ``man`` page or other online documentation.


Basic mirroring between two UNIX systems using ``ssh``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pulling a directory from a remote server::

  rsync -avH -e ssh user@server:test .

Here is a brief description of the above options (see the ``rsync man``
page for more details):

=======  =========================================================================
Option   Description
=======  =========================================================================
``-a``   archive mode; equals -rlptgoD (no -H,-A,-X)
``-v``   increase verbosity
``-H``   preserve hard links
``-e``   specify the remote shell to use
=======  =========================================================================

If you want to delete local files, which have been deleted
on the remote machine, simply add the ``--delete`` option::

  rsync -avH --delete -e ssh user@server:test .

Better remote shell options with ``ssh``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are going to be using the rsync command regularly
to transfer larger files, there are a number of options
to ``ssh`` that you should use::

  rsync -avH \
  -e 'ssh -ax -c blowfish -o ClearAllForwardings=yes' \
  user@server:test .

Here is a brief description of the above options (see the ``ssh man``
page for more details):

==================  =========================================================================
Option              Description
==================  =========================================================================
``-a``              Disables forwarding of the authentication agent connection.
``-x``              Disables X11 forwarding.
``-c cipher_spec``  Selects the cipher specification for encrypting the session.
``-o option``       Can be used to give options in the format used in the configuration file.
==================  =========================================================================

The ``blowfish`` cipher is used to make the encryption faster.
The option ``ClearAllForwardings`` is used to prevent possible automatic port forwards.

Example
~~~~~~~

On a remote machine, ``127.0.0.1``, new imaging data is being added
to a directory named ``/home/jarrod/Maryland/MRI`` by the ``jarrod``
account.  Another user, ``ttest`` wants to keep a local directory,
``/home/ttest/B-SNIP/Other-sites/Maryland/MRI`` on his machine in sync
with the remote directory.  ``ttest`` has an old copy of the remote directory
all ready and doesn't want to download everything again, but only the new or
changed files.

This is how ``test`` can use ``rsync`` to copy new or changed files to his
local directory from the remote server, while keeping local copies
of files that have been deleted from the remote server.

First ``ttest`` creates a couple of temporary variables to simplify his
commands and then changes into the directory where his local copy of the
data is::

  REMOTEUSER=jarrod
  REMOTEMACHINE=127.0.0.1
  REMOTEDIR=/home/jarrod/Maryland/MRI
  LOCALDIR=/home/ttest/B-SNIP/Other-sites/Maryland/MRI

``ttest`` can now start the transfer using the following command::

  rsync -avH \
  -e 'ssh -ax -c blowfish -o ClearAllForwardings=yes' \
  ${REMOTEUSER}@${REMOTEMACHINE}:${REMOTEDIR} ${LOCALDIR}

.. Tip:: It is always good practice to test commands before executing them.
         Many UNIX commands have a dry-run option, which perform a trial run
         with no changes made.  For example, the ``rsync`` command can be
         executed in a dry-run mode the ``-n`` option.


Here is a short script::

  #!/bin/bash

  REMOTEUSER=jarrod
  REMOTEMACHINE=127.0.0.1

  for SITE in Maryland Hartford Detroit
  do
    REMOTEDIR=/home/jarrod/${SITE}/MRI
    LOCALDIR=/home/ttest/B-SNIP/Other-sites/${SITE}/MRI
    echo "Synching ${REMOTEDIR}..."
    rsync -avH \
      -e 'ssh -ax -c blowfish -o ClearAllForwardings=yes' \
      ${REMOTEUSER}@${REMOTEMACHINE}:${REMOTEDIR} ${LOCALDIR}
  done

  REMOTEDIR=/home/jarrod/Chicago
  LOCALDIR=/home/ttest/B-SNIP/Other-sites/Chicago
  echo "Synching ${REMOTEDIR}..."
  rsync -avH \
    -e 'ssh -ax -c blowfish -o ClearAllForwardings=yes' \
    ${REMOTEUSER}@${REMOTEMACHINE}:${REMOTEDIR} ${LOCALDIR}
