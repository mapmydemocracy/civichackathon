
import csv

import common


def main():
    base_name = "candidates.csv"
    for line in common.csv_lines(base_name):
        print(line)


if __name__=='__main__':
    main()
