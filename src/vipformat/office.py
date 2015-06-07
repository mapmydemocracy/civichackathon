
import csv

from vipformat import candidate, common, electoralDistrict


def make_office_id(number):
    return 'office_{0}'.format(number)

def emitOffice(line, office_id):
    d = [
        ('ElectoralDistrictId', line[5]),
        ('Name', '<Text language="en">'+line[1]+'</Text>'),
    ]
    return common.pairlistToXml('Office', d, object_id=office_id)

def emitContest(line, candidateIds, office_id):
    object_id = 'contest_{0}'.format(line[0])
    contest_name = line[1]
    d = []
    for candidate_id in candidateIds:
        selection_id = candidate.make_selection_id(candidate_id)
        d.append(('BallotSelectionId', selection_id))
    d.extend([
        ('ElectoralDistrictId', line[5]),
        ('Name', contest_name),
        ('NumberElected', '1'),
        ('OfficeId', office_id),
        ('VotesAllowed', '1'),
    ])

    return common.pairlistToXml('CandidateContest', d, object_id=object_id)

def getCandsForOffices():
    ret = {}
    base_name = 'candidates.csv'
    for line in common.csv_lines(base_name):
        personId = line[0]
        officeId = make_office_id(line[2])
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
        office_id = make_office_id(line[0])
        if office_id in candsForOffices:
            ret += emitOffice(line, office_id=office_id)
            ret += emitContest(line, candsForOffices[office_id], office_id=office_id)
        
    return ret

if __name__=='__main__':
    print emitAllOffices()


