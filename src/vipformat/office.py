import csv
from VipFormat import common, electoralDistrict

def emitOffice(line):
    d = [
        ('Office', line[1], 
        ('Max_Terms', line[2],
        ('Term_Length(Years)', line[3], 
        ('ElectoralDistrict', line[5]))))
    ]
    return common.pairlistToXml('OfficeID', 'id="'+line[0]+'"', d)
def emitAllOffices():
    ret = ''
    base_name = "offices.csv"
    for line in common.csv_lines(base_name):
        ret += emitOffice(line)
    return ret

#def main(): 
#    csvFile = "/home/dennis/hackforSF/civichackathon/data/offices.csv"
#    xmlFile = "office.xml"
#
#    csvData = csv.reader(open(csvFile))
#    xmlData = open(xmlFile, 'w') 
#
#    xmlData.write('<?xml version="1.0"?>' + "\n")
#    # there must be only one top-level tag
#    xmlData.write('<csv_data>' + "\n")
#
#    rowNum = 0
#    for row in csvData:
#        if rowNum == 0:
#            tags = row
#            #replace spaces w/ underscores in tag names
#            for i in range(len(tags)):
#                tags[i] = tags[i].replace(' ', '_')
#        else:
#            xmlData.write('<row>' + "\n")
#            for i in range(len(tags)):
#                xmlData.write('    ' + '<'+  tags[i] + '>' + row[i] + '</' + tags[i] + '>' + "\n")
#            xmlData.write('</row>' + "\n")
#
#        rowNum += 1
#
#    xmlData.write('</csv_data>' + "\n")
#    xmlData.close()

if __name__=='__main__':
    main()

