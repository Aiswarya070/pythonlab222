import csv
csv_file1=open('studentdetails - studentdetails.csv','r')
csv_reader=csv.reader(csv_file1)
for line in csv_reader:
    #print(line[3])
    print(line)
    
    