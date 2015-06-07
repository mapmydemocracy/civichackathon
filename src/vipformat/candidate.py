
"""


<xs:complexType name="Candidate">
  <xs:sequence>
    <xs:element name="BallotName" type="InternationalizedText" />
    <xs:element name="ExternalIdentifiers" type="ExternalIdentifiers" minOccurs="0" />
    <xs:element name="FileDate" type="xs:dateTime" minOccurs="0" />
    <xs:element name="IsIncumbent" type="xs:boolean" minOccurs="0" />
    <xs:element name="IsTopTicket" type="xs:boolean" minOccurs="0" />
    <xs:element name="PartyId" type="xs:IDREF" minOccurs="0" />
    <xs:element name="PersonId" type="xs:IDREF" minOccurs="0" />
    <xs:element name="PostElectionStatus" type="CandidatePostElectionStatus" minOccurs="0" />
    <xs:element name="PreElectionStatus" type="CandidatePreElectionStatus" minOccurs="0" />
    <xs:element name="SequenceOrder" type="xs:integer" minOccurs="0" />
  </xs:sequence>
  <xs:attribute name="id" type="xs:ID" use="required" />
</xs:complexType>

<xs:complexType name="Person">
  <xs:sequence>
    <xs:element name="ContactInformation" type="ContactInformation" minOccurs="0" maxOccurs="unbounded" />
    <xs:element name="DateOfBirth" type="xs:date" minOccurs="0" />
    <xs:element name="FirstName" type="xs:string" minOccurs="0" />
    <xs:element name="FullName" type="InternationalizedText" minOccurs="0" />
    <xs:element name="LastName" type="xs:string" minOccurs="0" />
    <xs:element name="MiddleName" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
    <xs:element name="Nickname" type="xs:string" minOccurs="0" />
    <xs:element name="PartyId" type="xs:IDREF" minOccurs="0" />
    <xs:element name="Prefix" type="xs:string" minOccurs="0" />
    <xs:element name="Profession" type="InternationalizedText" minOccurs="0" />
    <xs:element name="Suffix" type="xs:string" minOccurs="0" />
    <xs:element name="Title" type="InternationalizedText" minOccurs="0" />
  </xs:sequence>
  <xs:attribute name="id" type="xs:ID" use="required" />
</xs:complexType>


"""
import csv
from datetime import datetime

from vipformat import common
from vipformat.common import pairlistToXml


def make_selection_id(person_number):
    return "selection_{0}".format(person_number)


def make_contact_info(line, person_id):
    """
    <xs:complexType name="ContactInformation">
      <xs:sequence>
        <xs:element name="AddressLine" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Email" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Fax" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
        <!-- Note: The "Hours" element is being deprecated and will be removed
             in future versions of VIP.
          -->
        <xs:element name="Hours" type="InternationalizedText" minOccurs="0" />
        <xs:element name="HoursOpenId" type="xs:IDREF" minOccurs="0" />
        <!-- This can be a person or place name. -->
        <xs:element name="Name" type="xs:string" minOccurs="0" />
        <xs:element name="Phone" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Uri" type="xs:anyURI" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
      <xs:attribute name="identifier" type="xs:string" use="required" />
    </xs:complexType>
    """
    address = line[5]
    email = line[7]
    phone = line[6]
    d = [
        ('AddressLine', address),
        ('Email', email),
        ('Phone', phone),
    ]
    xml = pairlistToXml('ContactInformation', d, identifier=person_id)
    return xml


def line_to_xml(line):
    """
    Fields:
      PersonId, Office, Office_ID, CandidatePreElectionStatus, Name,
      Address & Zip, Telephone, Email, FileDate
    """
    person_number = line[0]
    person_id = "person_{0}".format(person_number)

    file_dt = line[8]
    if file_dt:
        dt_parts = [int(n) for n in line[8].split("-")]  # year, month, day
        file_date_time = datetime(*dt_parts)
        file_date = common.make_xml_datetime(file_date_time)
    else:
        file_date = ''

    name = line[4]
    pre_election_status = line[3]

    # Person object
    contact_info_xml = make_contact_info(line, person_id=person_id)
    d = [
        contact_info_xml,
        ('Name', name),
    ]
    xml = pairlistToXml('Person', d, object_id=person_id)

    # Candidate object
    candidate_id = "candidate_{0}".format(person_number)
    d = [
        common.make_xml_internationalized('BallotName', name),
        ('FileDate', file_date),  # This is actually xs:dateTime.
        ('PersonId', person_id),
        ('PreElectionStatus', pre_election_status),
    ]
    xml += pairlistToXml('Candidate', d, object_id=candidate_id)

    # CandidateSelection object
    selection_id = make_selection_id(person_number)
    d = [
        ('CandidateId', candidate_id),
    ]
    xml += pairlistToXml('CandidateSelection', d, object_id=selection_id)

    return xml


def parse_candidates():
    base_name = "candidates.csv"
    xml = ''
    for line in common.csv_lines(base_name):
        xml += line_to_xml(line)

    return xml


if __name__=='__main__':
    make_candidates_xml()
