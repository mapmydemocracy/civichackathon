
import csv

from vipformat import common, electoralDistrict

officeCsvFile = '../../data/offices.csv'

def emitOffice(line):
    object_id = line[0]
    d = [
        ('ElectoralDistrictID', line[5]),
        ('Name', '<Text language="en">'+line[1]+'</Text>'),
    ]
    return common.pairlistToXml('Office', d, object_id=object_id)

def emitContest(line):
    object_id = line[0]
    d = [
        ('BallotTitle', '<Text language="en">'+line[1]+'</Text>'),
        ('ElectoralDistrictID', line[5]),
        ('NumberElected', '1'),
        ('VotesAllowed', '1'),
        ('OfficeID', line[0])
    ]
    return common.pairlistToXml('CandidateContest', d, object_id=object_id)

def emitAllOffices():
    ret = ''
    base_name = 'offices.csv'
    for line in common.csv_lines(base_name):
        ret += emitOffice(line)
        ret += emitContest(line)
        
    return ret

if __name__=='__main__':
    print emitAllOffices()


