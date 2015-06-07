
from vipformat import common


SF_BOS_DISTRICT_TYPE = 'BOS'
SF_DISTRICT_ID = 'district_sf'
electoralDistricts = {}

def make_district_id(district_type, district_number):
    if district_type == 'SF':
        return SF_DISTRICT_ID
    num = int(district_number)
    if district_type == SF_BOS_DISTRICT_TYPE:
        return 'district_bos_' + "{0:02d}".format(num)
    else:
        raise Exception("unknown district type: {0}".format(district_type))

def make_district_id_supervisor(num):
    return make_district_id(SF_BOS_DISTRICT_TYPE, num)

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
