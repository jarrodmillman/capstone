.. _cut:

cut
===

**Name**

``cut - remove sections from each line of files``

**Synopsis**

``cut OPTION... [FILE]...``

**Description**

Print selected parts of lines from each FILE to standard output.

Mandatory  arguments  to  long  options  are  mandatory  for short
options too.

-b, --bytes=LIST
       select only these bytes

-c, --characters=LIST
       select only these characters

-d, --delimiter=DELIM
       use DELIM instead of TAB for field delimiter

-f, --fields=LIST
       select only these fields;  also print any line that contains
       no delimiter character, unless the -s option is specified

Use  one,  and  only one of -b, -c or -f.  Each LIST is made up of
one range, or many ranges separated by commas.  Selected input  is
written  in the same order that it is read, and is written exactly
once.  Each range is one of:

N      N'th byte, character or field, counted from 1

N-     from N'th byte, character or field, to end of line

N-M    from N'th to M'th (included) byte, character or field

-M     from first to M'th (included) byte, character or field

With no FILE, or when FILE is -, read standard input.
