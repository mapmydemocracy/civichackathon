
import csv

import common


def make_candidate_xml(line):
    office = line[0]
    name = line[2]
    print(office, name)


def make_candidates_xml():
    base_name = "candidates.csv"
    for line in common.csv_lines(base_name):
        make_candidate_xml(line)


if __name__=='__main__':
    make_candidates_xml()
