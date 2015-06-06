
import common


electoralDistricts = {}

districtName_city = 'SF_city'
def districtName_supervisor(num):
    return 'SF_'+num

def emitCitywideDistrict():
    d = [
        ('name', 'San Francisco city'),
        ('type', 'city')
    ]
    return common.pairlistToXml('ElectoralDistrict', d, object_id=districtName_city)

def emitSupervisorDistrict(name):
    d = [
        ('name', 'San Francisco supervisor district '+name),
        ('number', name),
        ('type', 'city-supervisor'),
    ]
    object_id = districtName_supervisor(name)
    return common.pairlistToXml('ElectoralDistrict', d, object_id=object_id)

    
def emitAllElectoralDistricts():
    ret = emitCitywideDistrict()
    for i in range(1,12):
        ret = ret + emitSupervisorDistrict(str(i))
    return ret

if __name__=='__main__':
    print emitAllElectoralDistricts()
