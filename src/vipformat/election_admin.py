"""Supports creating the ElectionsAdministration object."""

import csv
from vipformat import common
from vipformat.common import pairlistToXml


SF_ELECTION_ADMIN_ID = "election_admin_1"

def make_contact_info_xml():
    """
    <xs:complexType name="ContactInformation">
      <xs:sequence>
        <xs:element name="AddressLine" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Email" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Fax" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="HoursOpenId" type="xs:IDREF" minOccurs="0" />
        <!-- This can be a person or place name. -->
        <xs:element name="Name" type="xs:string" minOccurs="0" />
        <xs:element name="Phone" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="Uri" type="xs:anyURI" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
      <xs:attribute name="identifier" type="xs:string" use="required" />
    </xs:complexType>
    """
    identifier = "contact_info_department"
    d = [
        ("AddressLine", "Department of Elections"),
        ("AddressLine", "1 Dr. Carlton B. Goodlett Place, Room 48"),
        ("AddressLine", "San Francisco, CA 94102"),
        ("Fax", "(415) 554-7344"),
        ("Name", "San Francisco Department of Elections"),
        # TODO: Add TTY number when VIP starts supporting TTY phone numbers:
        #   https://github.com/votinginfoproject/vip-specification/issues/242
        ("Phone", "(415) 554-4375"),
        ("Uri", "http://sfelections.org"),
    ]
    xml = pairlistToXml('ContactInformation', d, identifier=identifier)
    return xml

def make_department_xml():
    """
    <xs:element name="Department" maxOccurs="unbounded">
      <xs:complexType>
        <xs:sequence>
          <xs:element name="ContactInformation" type="ContactInformation" minOccurs="0" />
          <xs:element name="ElectionOfficialPersonId" type="xs:IDREF" minOccurs="0" />
          <xs:element name="VoterService" minOccurs="0" maxOccurs="unbounded">
          ...
          </xs:element>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    """
    contact_info_xml = make_contact_info_xml()
    d = [contact_info_xml]
    xml = pairlistToXml('Department', d)

    return xml

def make_person_info_xml():
    """
    <Person id="per50001">
        <ContactInformation identifier="ci60002">
            <Email>rwashburne@albemarle.org</Email>
            <Phone>4349724173</Phone>
        </ContactInformation>
        <FirstName>RICHARD</FirstName>
        <LastName>WASHBURNE</LastName>
        <MiddleName>J.</MiddleName>
        <Nickname>JAKE</Nickname>
        <Title>
            <Text language="en">General Registrar Physical</Text>
        </Title>
    </Person>
    """
    identifier = "person_director"
    d = [
        ("FirstName", "JOHN"), 
        ("LastName", "ARNTZ"),
        ("Title", "Director of Elections"),
    ]
    xml = pairlistToXml('ElectionAdministration', d, identifier=identifier)
    return xml

def make_election_administration_xml():
    """
    <xs:complexType name="ElectionAdministration">
      <xs:sequence>
        <xs:element name="AbsenteeUri" type="xs:anyURI" minOccurs="0" />
        <xs:element name="AmIRegisteredUri" type="xs:anyURI" minOccurs="0" />
        <!-- A locality may have more than one department with each handling different services. -->
        <xs:element name="Department" maxOccurs="unbounded">
        ...
        </xs:element>
        <xs:element name="ElectionsUri" type="xs:anyURI" minOccurs="0" />
        <xs:element name="RegistrationUri" type="xs:anyURI" minOccurs="0" />
        <xs:element name="RulesUri" type="xs:anyURI" minOccurs="0" />
        <xs:element name="WhatIsOnMyBallotUri" type="xs:anyURI" minOccurs="0" />
        <xs:element name="WhereDoIVoteUri" type="xs:anyURI" minOccurs="0" />
      </xs:sequence>
      <xs:attribute name="id" type="xs:ID" use="required" />
    </xs:complexType>
    """
    department_xml = make_department_xml()
    person_xml = make_person_info_xml()
    d = [
        department_xml,
        ("ElectionsUri", "http://sfelections.org"),
        person_xml,
    ]
    xml = pairlistToXml('ElectionAdministration', d, object_id=SF_ELECTION_ADMIN_ID)

    return xml
