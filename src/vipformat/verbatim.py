
from vipformat import common

def emitVerbatim():
    return """<Locality id="{locality_id}">
  <ElectionAdministrationId>0</ElectionAdministrationId>
  <ExternalIdentifiers>
    <ExternalIdentifier>
      <Type>ocd-id</Type>
      <Value>ocd-division/country:us/state:va/county:san francisco/city:san francisco</Value>
    </ExternalIdentifier>
  </ExternalIdentifiers>
  <Name>San Francisco</Name>
  <Type>county</Type>
</Locality>
""".format(locality_id=common.SF_LOCALITY_ID)
