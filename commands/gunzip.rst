.. _gunzip:

gunzip
======

**Name**

``gunzip - compress or expand files``

**Synopsis**

``gunzip [option]``

**Description**

gunzip takes a list of files on its command line and replaces each
file whose name ends with .gz, -gz, .z, -z, \_z or .Z and which
begins with the correct magic number with an uncompressed file
without the original extension. gunzip can currently decompress
files created by gzip, zip, compress, compress -H or pack.
