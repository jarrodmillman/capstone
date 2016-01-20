.. _split:

split
=====

**Name**

split -- split a file into pieces

**Synopsis**

**split** [options...] {infile} {outfile}

**Description**

Split INFILE into a specified number of line groups, with output
going into a succession of files, OUTFILEaa, OUTFILEab, and so on.
The INFILE remains unchanged. This command is handy if you have a
very long text file that needs to be reduced to a succession of
smaller files. This was often done to email large files in smaller
chunks, because it was at one time considered bad practice to send
single large email messages.


-n
    Split the INFILE into *n*-line segments. The default is 1000.



