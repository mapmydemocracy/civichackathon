
# specialized for the San Francisco precinct list

import csv

from vipformat import common, electoralDistrict


def emitPrecinct(line, precinct_ids):
    precinct_id = "precinct_{0}".format(line[0])
    # Some precincts occur more than once, for example Pct 7509/7511.
    if precinct_id in precinct_ids:
        return ''
    precinct_ids.add(precinct_id)
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
    # Create set to prevent duplicates.
    precinct_ids = set()
    for line in common.csv_lines(base_name):
        ret += emitPrecinct(line, precinct_ids)

    return ret

if __name__=='__main__':
    print emitAllPrecincts()
