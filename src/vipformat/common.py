
import csv
import os
import textwrap


# VIP recommends 2-space indents.
INDENT = 2 * ' '

def indent(text):
    lines = text.splitlines(True)
    glue = INDENT
    text = INDENT + INDENT.join(lines)

    return text


def csv_lines(base_name):
    """Iterate over lines of a CSV file.

    Usage:

        for line in csv_lines(base_name):
            do_stuff(line)

    """
    path = os.path.join('data', base_name)
    with open(path, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        # Skip header line.
        next(csvreader)
        for line in csvreader:
            yield line

def make_attr(key, value):
    return '{0}="{1}"'.format(key, value)

def pairlistToXml(elemName, contents, object_id=None, identifier=None):
    attrs = ''
    if object_id is not None:
        attrs += ' {0}'.format(make_attr('id', object_id))
    if identifier is not None:
        attrs += ' {0}'.format(make_attr('identifier', identifier))

    ret = "<{0}{1}>\n".format(elemName, attrs)
    for item in contents:
        if isinstance(item, basestring):
            inner = item
        else:
            tag, value = item
            inner = '<{tag}>{value}</{tag}>\n'.format(tag=tag, value=value)
        ret += indent(inner)
    ret += '</{0}>\n'.format(elemName)

    return ret
