
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
    return common.pairlistToXml('ElectoralDistrict', 'id="'+districtName_city+'"', d)

def emitSupervisorDistrict(name):
    d = [
        ('name', 'San Francisco supervisor district '+name),
        ('number', name),
        ('type', 'city-supervisor'),
    ]
    return common.pairlistToXml('ElectoralDistrict', 'id="'+districtName_supervisor(name)+'"', d)

    
def emitAllElectoralDistricts():
    ret = emitCitywideDistrict()
    for i in range(1,12):
        ret = ret + emitSupervisorDistrict(str(i))
    return ret

if __name__=='__main__':
    print emitAllElectoralDistricts()
