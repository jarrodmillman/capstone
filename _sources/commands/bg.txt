.. _bg:

bg
==

**Name**

``bg - background``

**Synopsis**

``bg [jobspec]``

**Description**

Place JOBSPEC in the background, as if it had been started with &.
If JOBSPEC is not present, then the shell's notion of the
*current job* is used, as indicated by the plus sign (+) in output
from the *jobs* command. Using this command on a job that is
stopped will allow it to run in the background.
