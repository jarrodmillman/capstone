#!/usr/bin/env python
""" Process ipython notebook to plot-directived, doctested rst
"""

import sys
from os.path import splitext
from warnings import warn

import nbformat
from nbconvert import RSTExporter


def line_indent(line):
    return len(line) - len(line.lstrip())


def is_empty(line):
    return line.strip() == ''


def proc_body(body, indent):
    spaces = ' ' * indent
    new_body = ['.. plot::\n', spaces + ':context:\n']
    plts = [line for line in body if line.strip().startswith('plt.')]
    if len(plts) == 0:
        new_body.append(spaces + ':nofigs:\n')
    new_body.append('\n')
    # Ignore trailing blank lines
    n_good = len(body)
    for line in body[::-1]:
        if not is_empty(line):
            break
        n_good -= 1

    for line in body[:n_good]:
        if is_empty(line):
            new_body.append(line)
            continue
        L_indent = line_indent(line)
        if L_indent == indent:
            new_line = spaces + '>>> ' + line.lstrip()
            new_body.append(new_line)
            continue
        extra_spaces = ' ' * (L_indent - indent)
        new_line = spaces + '... ' + extra_spaces + line.lstrip()
        new_body.append(new_line)
    return new_body


def _p_default(line, new_contents):
    if line.startswith('.. code:: python'):
        return 'code-block-line0'
    elif not line.startswith('.. image::'):
        # Discard image lines
        new_contents.append(line)
    return 'default'


def proc_notebook(contents):
    new_contents = []
    state = 'default'
    for line in contents:
        if state == 'default':
            state = _p_default(line, new_contents)
            continue
        if state == 'code-block-line0':
            if line.strip() == '':
                continue
            block_indent = line_indent(line)
            block_body = []
            state = 'code-block-body'
        if state == 'code-block-body':
            if not is_empty(line) and line_indent(line) < block_indent:
                state = 'waiting-for-pl'
                new_contents += proc_body(block_body, block_indent)
            block_body.append(line)
        if state == 'waiting-for-pl':
            if line.startswith('.. parsed-literal::'):
                state = 'in-pl-line0'
                continue
            new_contents.append('\n')  # Restore trailing blank
            new_contents.append(line)
            state = 'default'
        if state == 'in-pl-line0':
            if is_empty(line):
                continue
            pl_indent = line_indent(line)
            state = 'in-pl'
        if state == 'in-pl':
            if not is_empty(line) and line_indent(line) < pl_indent:
                state = _p_default(line, new_contents)
                continue
            if line.strip().startswith('<matplotlib.'):
                line = ' ' * line_indent(line) + '<...>\n'
            elif line.strip().startswith('[<matplotlib.'):
                line = ' ' * line_indent(line) + '[...]\n'
            new_contents.append(line)

    return new_contents


def nb2rst(filepath):
    with open(filepath) as fh:
        nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)
    exporter = RSTExporter()
    # source is a tuple of python source code
    # meta contains metadata
    source, meta = exporter.from_notebook_node(nb)
    return [line + '\n' for line in source.split('\n')]


def main():
    for ipynb_fname in sys.argv[1:]:
        froot, ext = splitext(ipynb_fname)
        if ext == '.rst':
            raise RuntimeError('Expecting ipynb file as input, got ' +
                               ipynb_fname)
        contents = nb2rst(ipynb_fname)
        better_contents = proc_notebook(contents)
        new_fname = froot + '.rst'
        with open(new_fname, 'wt') as fobj:
            fobj.write(''.join(better_contents))


if __name__ == '__main__':
    warn('Please use nb2plots instead of this tool'
         ': https://pypi.python.org/pypi/nb2plots')
    main()
