
import csv

import common


def main():
    base_name = "precincts_20140321.csv"
    for line in common.csv_lines(base_name):
        print(line)


if __name__=='__main__':
    main()
