
import precinct
import electoralDistrict


def emitProlog():
    print '<?xml version="1.0"?>'
    print '<VipObject xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="5.0" xsi:noNamespaceSchemaLocation="http://votinginfoproject.github.com/vip-specification/vip_spec.xsd">'

def emitEpilog():
    print '</VipObject>'

def emitAll():
    emitProlog()
    precinct.emitAllPrecincts()
    electoralDistrict.emitAllElectoralDistricts()
    emitEpilog()

if __name__=='__main__':
    emitAll()
