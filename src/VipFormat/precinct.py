
# specialized for the San Francisco precinct list

import csv
import common
import electoralDistrict


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
    with open('../../data/precincts_20140321.csv', 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            if line[0] != 'VotingPrecinctID':   # ignore header line
                ret = ret + emitPrecinct(line)
    return ret

if __name__=='__main__':
    print emitAllPrecincts()
