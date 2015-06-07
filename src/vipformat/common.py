
import csv
import os


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

    ret = '<' + elemName
    if attrs:
        ret += attrs
    ret += '>\n'
    for (k,v) in contents:
        ret = ret + '    <' + k + '>' + v + '</' + k + '>\n'
    ret = ret + '</' + elemName + '>\n'
    return ret
