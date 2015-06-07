
import common


districtName_city = 'SF'
electoralDistricts = {}

def districtName_supervisor(num):
    num = int(num)
    return 'SF_' + "{0:02d}".format(num)

def emitCitywideDistrict():
    d = [
        ('Name', 'City and County of San Francisco'),
        ('Type', 'city')
    ]
    return common.pairlistToXml('ElectoralDistrict', d, object_id=districtName_city)

def emitSupervisorDistrict(name):
    d = [
        ('Name', 'San Francisco Supervisorial District ' + name),
        ('Number', name),
        ('Type', 'city-council'),
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
