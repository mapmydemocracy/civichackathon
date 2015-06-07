
# specialized for the San Francisco precinct list

import csv

from vipformat import common, electoralDistrict


def emitPrecinct(line):
    precinct_id = "precinct_{0}".format(line[0])
    bos_district = line[9]
    d = [
        ('ElectoralDistrictId', electoralDistrict.SF_DISTRICT_ID),
        ('ElectoralDistrictId', electoralDistrict.make_district_id_supervisor(bos_district)),
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
