.. _gzip:

gzip
====

**Name**

``gzip - compress or expand files``

**Synopsis**

``gzip [option]``

**Description**

Gzip reduces the size of the named files using Lempel-Ziv coding
(LZ77). Whenever possible, each file is replaced by one with the
extension .gz, while keeping the same ownership modes, access and
modification times.

-d, --decompress, --uncompress 
    Decompress

-#, --fast, --best 
    Regulate the speed of compression using the specified digit #,
    where -1 or --fast indicates the fastest compression method (less
    compression) and -9 or --best indicates the slowest compression
    method (best compression). The default compression level is -6
    (that is, biased towards high compression at expense of speed).

-c, --stdout, --to-stdout 
    Write output on standard output; keep original files unchanged. If
    there are several input files, the output consists of a sequence of
    independently compressed members. To obtain better compression,
    concatenate all input files before compressing them.
