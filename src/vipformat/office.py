import csv
from vipformat import common, electoralDistrict

def emitOffice(line):
    object_id = line[0]
    d = [
        ('OfficeHolderPersonId', line[1]), 
        ('Name', line[5])]
    return common.pairlistToXml('Office', d, object_id=object_id)
    
def emitAllOffices():
    ret = ''
    base_name = "offices.csv"
    for line in common.csv_lines(base_name):
        ret += emitOffice(line)
    return ret

if __name__=='__main__':
    print emitAllOffices()
