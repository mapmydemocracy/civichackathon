
from vipformat.common import indent
from vipformat import candidate, common, electoralDistrict, office, precinct, verbatim


def emitProlog():
    return '<?xml version="1.0"?>\n<VipObject xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="5.0" xsi:noNamespaceSchemaLocation="http://votinginfoproject.github.com/vip-specification/vip_spec.xsd">\n'

def emitEpilog():
    return '</VipObject>\n'

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
    state_id = 'state_ca'
    d = [
        ('Name', 'California'),
    ]
    xml = common.pairlistToXml('State', d, object_id=state_id)

    return xml

def emitAll():
    ret = emitProlog()
    ret += indent(make_states())
    ret += precinct.emitAllPrecincts()
    ret += electoralDistrict.emitAllElectoralDistricts()
    ret += candidate.parse_candidates()
    ret += office.emitAllOffices()
    ret += verbatim.emitVerbatim()
    ret += emitEpilog()
    return ret

if __name__=='__main__':
    print emitAll()
