
import csv
import os


def csv_lines(base_name):
    """Iterate over lines of a CSV file.

    Usage:

        for line in csv_lines(base_name):
            do_stuff(line)

    """
    path = os.path.join('../../data', base_name)
    with open(path, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        # Skip header line.
        next(csvreader)
        for line in csvreader:
            yield line
