"""
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
from vipformat import common, electoralDistrict
from vipformat.common import pairlistToXml

def emitOffice():
    object_id = ""
    d = [
    	('Department', "Elections"), 
        ('ContactInformation', 
        	("Address", "1 Dr. Carlton B. Goodlett Place, Room 48 San Francisco, CA 94102"),
    ]
    return common.pairlistToXml('ElectionAdministration', d, object_id=object_id)
    
def line_to_xml():
    """
    Fields:
        Department, ContactInformation, Address, Phone, Fax, TTY
    """
    
    #ContactInformation object
    d = [
        ('Address', "1 Dr. Carlton B. Goodlett Place, Room 48 San Francisco, CA 94102"),
    	("Phone", "(415) 554-4375"), 
     	("Fax", "(415) 554-7344"), 
        ("TTY", "(415) 554-4386"),
    ]
    xml = pairlistToXml("ContactInformation", d, object_id=person_id)

    return xml

             
if __name__=='__main__':
    print emitOffice()
