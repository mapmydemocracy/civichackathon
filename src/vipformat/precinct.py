
# specialized for the San Francisco precinct list

import csv

from vipformat import common, electoralDistrict


def emitPrecinct(line):
    precinct_id = "precinct_{0}".format(line[0])
    d = [
        ('ElectoralDistrictId', electoralDistrict.districtName_city),
        ('ElectoralDistrictId', electoralDistrict.districtName_supervisor(line[9])),
        ('LocalityId', common.SF_LOCALITY_ID),
        ('Name', line[1]),
    ]
    return common.pairlistToXml('Precinct', d, object_id=precinct_id)

def emitAllPrecincts():
    ret = ''
    base_name = "precincts_20140321.csv"
    for line in common.csv_lines(base_name):
        ret += emitPrecinct(line)

    return ret

if __name__=='__main__':
    print emitAllPrecincts()
