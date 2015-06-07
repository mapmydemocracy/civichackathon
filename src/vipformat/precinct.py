
# specialized for the San Francisco precinct list

import csv

from vipformat import common, electoralDistrict


def emitPrecinct(line):
    object_id = line[0]
    d = [
        ('name', line[1]),
        ('LocalityId', common.SF_LOCALITY_ID),
        ('ElectoralDistrictId', electoralDistrict.districtName_city),
        ('ElectoralDistrictId', electoralDistrict.districtName_supervisor(line[9])),
    ]
    return common.pairlistToXml('Precinct', d, object_id=object_id)

def emitAllPrecincts():
    ret = ''
    base_name = "precincts_20140321.csv"
    for line in common.csv_lines(base_name):
        ret += emitPrecinct(line)

    return ret

if __name__=='__main__':
    print emitAllPrecincts()
