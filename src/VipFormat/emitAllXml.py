
import precinct
import electoralDistrict


def emitProlog():
    return '<?xml version="1.0"?>\n<VipObject xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="5.0" xsi:noNamespaceSchemaLocation="http://votinginfoproject.github.com/vip-specification/vip_spec.xsd">\n'

def emitEpilog():
    return '</VipObject>\n'

def emitAll():
    ret = emitProlog()
    ret = ret + precinct.emitAllPrecincts()
    ret = ret + electoralDistrict.emitAllElectoralDistricts()
    ret = ret + emitEpilog()
    return ret

if __name__=='__main__':
    print emitAll()
