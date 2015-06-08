"""
Supports creating the ElectionsAdministration object:

<xs:complexType name="ElectionAdministration">
  <xs:sequence>
    <xs:element name="AbsenteeUri" type="xs:anyURI" minOccurs="0" />
    <xs:element name="AmIRegisteredUri" type="xs:anyURI" minOccurs="0" />
    <!-- A locality may have more than one department with each handling different services. -->
    <xs:element name="Department" maxOccurs="unbounded">
      <xs:complexType>
        <xs:sequence>
          <xs:element name="ContactInformation" type="ContactInformation" minOccurs="0" />
          <xs:element name="ElectionOfficialPersonId" type="xs:IDREF" minOccurs="0" />
          <xs:element name="VoterService" minOccurs="0" maxOccurs="unbounded">
            <xs:complexType>
              <xs:all>
                <!--
                    The contact information below can be used to override or
                    add specific fields to the base Departmental contact information if
                    the service has different information.  For example, if the voter
                    service has its own phone number, the ContactInformation object
                    below can be an object containing only a Phone element.
                  -->
                <xs:element name="ContactInformation" type="ContactInformation" minOccurs="0" />
                <xs:element name="Description" type="InternationalizedText" minOccurs="0" />
                <!--
                    This is for use if a certain person handles the particular service,
                    for example a contact person for overseas voting.
                  -->
                <xs:element name="ElectionOfficialPersonId" type="xs:IDREF" minOccurs="0" />
                <xs:element name="Type" type="VoterServiceType" minOccurs="0" />
                <xs:element name="OtherType" type="xs:string" minOccurs="0" />
              </xs:all>
            </xs:complexType>
          </xs:element>
        </xs:sequence>
      </xs:complexType>
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


import csv
from vipformat import common
from vipformat.common import pairlistToXml


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

def make_election_administration_xml():
    """
    Fields:
        Department, ContactInformation, Address, Phone, Fax, TTY
    """
    election_admin_id = "election_admin_1"
    department_xml = make_department_xml()
    d = [department_xml]
    xml = pairlistToXml('ElectionAdministration', d, object_id=election_admin_id)

    return xml
