
electoralDistricts = {}

districtName_city = 'SF_city'
def districtName_supervisor(num):
    return 'SF_'+num

def emitCitywideDistrict():
    print '<ElectoralDistrict id="'+districtName_city+'">'
    print '    <name>San Francisco city</name>'
    print '    <type>city</type>'
    print '</ElectoralDistrict>'

def emitSupervisorDistrict(name):
    print '<ElectoralDistrict id="'+districtName_supervisor(name)+'">'
    print '    <name>San Francisco supervisor district '+name+'</name>'
    print '    <number>'+name+'</number>'
    print '    <type>city-supervisor</type>'    
    print '</ElectoralDistrict>'
    
def emitAllElectoralDistricts():
    emitCitywideDistrict()
    for i in range(1,12):
        emitSupervisorDistrict(str(i))

if __name__=='__main__':
    emitAllElectoralDistricts()
