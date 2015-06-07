
import csv

from vipformat import candidate, common, electoralDistrict


def make_office_id(number):
    return 'office_{0}'.format(number)

def emitOffice(line, office_id):
    """
    <xs:complexType name="Office">
      <xs:sequence>
        <xs:element name="ContactInformation" type="ContactInformation" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="ElectoralDistrictId" type="xs:IDREF" />
        <xs:element name="ExternalIdentifiers" type="ExternalIdentifiers" minOccurs="0" />
        <xs:element name="FilingDeadline" type="xs:date" minOccurs="0" />
        <xs:element name="IsPartisan" type="xs:boolean" minOccurs="0" />
        <xs:element name="Name" type="InternationalizedText" />
        <xs:element name="OfficeHolderPersonId" type="xs:IDREF" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Term" minOccurs="0">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="Type" type="OfficeTermType" />
              <xs:element name="StartDate" type="xs:date" minOccurs="0" />
              <xs:element name="EndDate" type="xs:date" minOccurs="0" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
      <xs:attribute name="id" type="xs:ID" use="required" />
    </xs:complexType>
    """
    district_type = line[5]
    district_number = line[6]
    district_id = electoralDistrict.make_district_id(district_type, district_number)
    d = [
        ('ElectoralDistrictId', district_id),
        ('Name', '<Text language="en">'+line[1]+'</Text>'),
    ]
    return common.pairlistToXml('Office', d, object_id=office_id)

def emitContest(line, candidateIds, office_id):
    """
    <xs:complexType name="ContestBase" abstract="true">
      <xs:sequence>
        <xs:element name="Abbreviation" type="xs:string" minOccurs="0" />
        <xs:element name="BallotSelectionId" type="xs:IDREF" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="BallotSubTitle" type="InternationalizedText" minOccurs="0" />
        <xs:element name="BallotTitle" type="InternationalizedText" minOccurs="0" />
        <xs:element name="ElectoralDistrictId" type="xs:IDREF" />
        <xs:element name="ElectorateSpecification" type="InternationalizedText" minOccurs="0" />
        <xs:element name="ExternalIdentifiers" type="ExternalIdentifiers" minOccurs="0" />
        <xs:element name="HasRotation" type="xs:boolean" minOccurs="0" />
        <xs:element name="Name" type="xs:string" />
        <xs:element name="SequenceOrder" type="xs:integer" minOccurs="0" />
        <xs:element name="VoteVariation" type="VoteVariation" minOccurs="0" />
        <xs:element name="OtherVoteVariation" type="xs:string" minOccurs="0" />
      </xs:sequence>
      <xs:attribute name="id" type="xs:ID" use="required" />
    </xs:complexType>
    """
    object_id = 'contest_{0}'.format(line[0])
    contest_name = line[1]
    vote_variation = line[7]
    d = []
    for candidate_id in candidateIds:
        selection_id = candidate.make_selection_id(candidate_id)
        d.append(('BallotSelectionId', selection_id))
    d.extend([
        ('ElectoralDistrictId', line[5]),
        ('Name', contest_name),
        ('VoteVariation', vote_variation),
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
