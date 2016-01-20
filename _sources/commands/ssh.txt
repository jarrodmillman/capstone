.. _ssh:

ssh
===

**Name**

``ssh -- OpenSSH SSH client``

**Synopsis**

``ssh [user@]hostname [command]``

**Description**

ssh (SSH client) is a program for logging into a remote machine and
for executing commands on a remote machine. It is intended to
replace rlogin and rsh, and provide secure encrypted communications
between two untrusted hosts over an insecure network.

ssh connects and logs into the specified hostname (with optional
user name).  The user must prove his/her identity to the remote
machine using one of several methods depending on the protocol
version used.

If command is specified, it is executed on the remote host instead
of a login shell.
