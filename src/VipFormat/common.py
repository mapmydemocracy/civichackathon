
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

def pairlistToXml(elemName, contents, object_id=None):
    elemParams = ''
    if object_id is not None:
        elemParams = 'id="{0}"'.format(object_id)
    ret = '<' + elemName
    if elemParams:
        ret = ret + ' ' + elemParams
    ret = ret + '>\n'
    for (k,v) in contents:
        ret = ret + '    <' + k + '>' + v + '</' + k + '>\n'
    ret = ret + '</' + elemName + '>\n'
    return ret
