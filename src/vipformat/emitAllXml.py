
import textwrap

from vipformat.common import indent
from vipformat import candidate, common, electoralDistrict, office, precinct, verbatim


CA_STATE_ID = 'state_ca'


def emitProlog():
    return '<?xml version="1.0"?>\n<VipObject xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="5.0" xsi:noNamespaceSchemaLocation="http://votinginfoproject.github.com/vip-specification/vip_spec.xsd">\n'


def emitEpilog():
    return '</VipObject>\n'


def make_locality():
    """
    <xs:complexType name="Locality">
      <xs:sequence>
        <xs:element name="ElectionAdministrationId" type="xs:IDREF" minOccurs="0" />
        <xs:element name="ExternalIdentifiers" type="ExternalIdentifiers" minOccurs="0" />
        <xs:element name="Name" type="xs:string" />
        <xs:element name="PollingLocationId" type="xs:IDREF" minOccurs="0" maxOccurs="unbounded" />
        <xs:element name="StateId" type="xs:IDREF" />
        <xs:element name="Type" type="DistrictType" />
        <xs:element name="OtherType" type="xs:string" minOccurs="0" />
      </xs:sequence>
      <xs:attribute name="id" type="xs:ID" use="required" />
    </xs:complexType>
    """
    external_identifiers_xml = textwrap.dedent("""\
    <ExternalIdentifiers>
      <ExternalIdentifier>
        <Type>ocd-id</Type>
        <Value>ocd-division/country:us/state:va/county:san francisco/city:san francisco</Value>
      </ExternalIdentifier>
    </ExternalIdentifiers>
    """)
    d = [
        ('ElectionAdministrationId', 0),
        external_identifiers_xml,
        ('Name', 'San Francisco'),
        ('Type', 'county'),
    ]
    xml = common.pairlistToXml('Locality', d, object_id=common.SF_LOCALITY_ID)

    return xml


def make_states():
    """
    <xs:complexType name="State">
      <xs:sequence>
        <xs:element name="ElectionAdministrationId" type="xs:IDREF" minOccurs="0" />
        <xs:element name="ExternalIdentifiers" type="ExternalIdentifiers" minOccurs="0" />
        <xs:element name="Name" type="xs:string" />
        <xs:element name="PollingLocationId" type="xs:IDREF" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
      <xs:attribute name="id" type="xs:ID" use="required" />
    </xs:complexType>
    """
    d = [
        ('Name', 'California'),
    ]
    xml = common.pairlistToXml('State', d, object_id=CA_STATE_ID)

    return xml


def emitAll():
    ret = emitProlog()
    ret += indent(make_states())
    ret += indent(precinct.emitAllPrecincts())
    ret += indent(electoralDistrict.emitAllElectoralDistricts())
    ret += indent(candidate.parse_candidates())
    ret += indent(office.emitAllOffices())
    ret += indent(make_locality())
    ret += emitEpilog()
    return ret


if __name__=='__main__':
    print emitAll()
