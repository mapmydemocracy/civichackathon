
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

def emitContest(line, candidateIds):
    object_id = line[0]
    d = [
        ('BallotTitle', '<Text language="en">'+line[1]+'</Text>'),
        ('ElectoralDistrictID', line[5]),
        ('NumberElected', '1'),
        ('VotesAllowed', '1'),
        ('OfficeID', line[0])
    ]
    for cand in candidateIds:
        d.append(('BallotSelectionId', cand))

    return common.pairlistToXml('CandidateContest', d, object_id=object_id)

def getCandsForOffices():
    ret = {}
    base_name = 'candidates.csv'
    for line in common.csv_lines(base_name):
        personId = line[0]
        officeId = line[2]
        if officeId in ret:
            ret[officeId].append(personId)
        else:
            ret[officeId] = [personId,]
    return ret

def emitAllOffices():
    candsForOffices = getCandsForOffices()

    ret = ''
    base_name = 'offices.csv'
    for line in common.csv_lines(base_name):
        officeId = line[0]
        if officeId in candsForOffices:
            ret += emitOffice(line)
            ret += emitContest(line, candsForOffices[officeId])
        
    return ret

if __name__=='__main__':
    print emitAllOffices()


