.. _pandoc:

pandoc
======

**Name**

``pandoc - general markup converter``

**Synopsis**

``pandoc [options] [input-file]...``

**Description**

Pandoc  is  a Haskell library for converting from one markup format to another,
and a command-line tool that uses this library.  It can read markdown and
(subsets of) Textile, reStructuredText, HTML, LaTeX, MediaWiki markup, TWiki
markup, Haddock markup, OPML, Emacs Org-mode, DocBook,  txt2tags,  EPUB  and
Word docx; and it can write plain text, markdown, reStructuredText, XHTML, HTML
5, LaTeX (including beamer slide shows), ConTeXt, RTF, OPML, DocBook,
OpenDocument, ODT, Word docx, GNU Texinfo, MediaWiki markup, DokuWiki markup,
Haddock markup, EPUB  (v2 or v3), FictionBook2, Textile, groff man pages, Emacs
Org-Mode, AsciiDoc, InDesign ICML, and Slidy, Slideous, DZSlides, reveal.js or
S5 HTML slide shows.  It can also produce PDF output on systems where LaTeX is
installed.

If no input-file is specified, input is read from stdin.  Otherwise, the
input-files are concatenated (with a blank line between each) and used as
input.  Output goes to stdout by default (though output to stdout is disabled
for the odt, docx, epub, and  epub3  output  formats).  For output to a file,
use the ``-o`` option::

       pandoc -o output.html input.txt

By default, pandoc produces a document fragment, not a standalone document
with a proper header and footer.  To produce a standalone document, use the
``-s`` or ``--standalone`` flag::

       pandoc -s -o output.html input.txt
