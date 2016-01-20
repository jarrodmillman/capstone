.. _tar:

tar
===

**Name**

tar -- The GNU version of the tar archiving utility

**Synopsis**

**tar** [options]

**Description**

tar is an archiving program designed to store and extract files
from an archive file known as a tarfile. A tarfile may be made on a
tape drive, however, it is also common to write a tarfile to a
normal file. The first argument to tar must be one of the options:
Acdrtux, followed by any optional functions. The final arguments to
tar are the names of the files or directories which should be
archived.


-t, --files-from=F
    get names to extract or create from file F

-c, --directory DIR
    change to directory DIR

-x, --exclude-from FILE
    exclude files listed in FILE

-V, --label NAME
    create archive with volume name NAME

-Z, --compress, --uncompress
    filter the archive through compress

-f, --file [hostname:]F
    use archive file or device F (default /dev/rmt0)


