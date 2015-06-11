"""Supports creating the Election Offical person ID."""

import csv
from vipformat import common
from vipformat.common import pairlistToXml


SF_ELECTION_ID = "election_person_1"

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