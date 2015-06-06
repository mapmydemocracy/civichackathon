
# specialized for the San Francisco precinct list

import csv

from VipFormat import common
from VipFormat import electoralDistrict


def emitPrecinct(line):
    d = [
        ('name', line[1]), 
        ('locality_id', line[9]), 
        ('ElectoralDistrictID', electoralDistrict.districtName_city),
        ('ElectoralDistrictID', electoralDistrict.districtName_supervisor(line[9])),
    ]
    return common.pairlistToXml('Precinct', 'id="'+line[0]+'"', d)

def emitAllPrecincts():
    ret = ''
    base_name = "precincts_20140321.csv"
    for line in common.csv_lines(base_name):
        ret += emitPrecinct(line)

    return ret

if __name__=='__main__':
    print emitAllPrecincts()
