
# specialized for the San Francisco precinct list

import csv

electoralDistrictAll = '0'


def emitPrecinct(line):
    print '<Precinct id='+line[0]+'>'
    print '   <name>'+line[1]+'</name>'
    print '   <locality_id>'+line[9]+'</locality_id>'
    print  '   <ElectoralDistrictID>'+electoralDistrictAll+'</ElectoralDistrictID>'
    print  '   <ElectoralDistrictID>'+line[9]+'</ElectoralDistrictID>'
    print '</Precinct>'

def emitAllPrecincts():
    with open('../../data/precincts_20140321.csv', 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            if line[0] != 'VotingPrecinctID':   # ignore header line
                emitPrecinct(line)

if __name__=='__main__':
    emitAllPrecincts()
