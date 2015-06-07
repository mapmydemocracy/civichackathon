
from vipformat import common


SF_DISTRICT_ID = 'district_sf'
electoralDistricts = {}

def make_district_id_supervisor(num):
    num = int(num)
    return 'district_bos_' + "{0:02d}".format(num)

def emitCitywideDistrict():
    d = [
        ('Name', 'City and County of San Francisco'),
        ('Type', 'city')
    ]
    return common.pairlistToXml('ElectoralDistrict', d, object_id=SF_DISTRICT_ID)

def emitSupervisorDistrict(number):
    name = 'San Francisco Supervisorial District {0}'.format(number)
    d = [
        ('Name', name),
        ('Number', number),
        ('Type', 'city-council'),
    ]
    district_id = make_district_id_supervisor(number)
    return common.pairlistToXml('ElectoralDistrict', d, object_id=district_id)

    
def emitAllElectoralDistricts():
    ret = emitCitywideDistrict()
    for i in range(1,12):
        ret = ret + emitSupervisorDistrict(str(i))
    return ret
