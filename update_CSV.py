import csv
fieldnames=[]
def changeData(filename, field1, val, field2, newvalue):
    fieldnames= getfield(filename)
    data = updatecsv(filename, field1, val, field2, newvalue)
    writecsv(filename, fieldnames, data)
 
def getfield(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for read in reader:
            head = read
            return head
def updatecsv(filename, field1, val, field2, newvalue):
    data=[]
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for read in reader:
            if(read[field1]==val):
                read[field2] = newvalue
            data.append(read)
        return data
def writecsv(filename, fieldnames, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
 