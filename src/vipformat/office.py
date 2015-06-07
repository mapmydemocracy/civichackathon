import csv
from vipformat import common, electoralDistrict

def emitOffice(line):
    object_id = line[0]
    d = [
        ('Office', line[1]), 
        ('Max_Terms', line[2]),
        ('Term_Length(Years)', line[3]), 
        ('ElectoralDistrict', line[5])]
    return common.pairlistToXml('OfficeID', d, object_id=object_id)
    
def emitAllOffices():
    ret = ''
    base_name = "offices.csv"
    for line in common.csv_lines(base_name):
        ret += emitOffice(line)
    return ret

if __name__=='__main__':
    print emitAllOffices()
