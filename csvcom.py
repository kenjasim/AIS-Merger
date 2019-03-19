import csv
n = '5'
mmsil = []
csvl = []
#open the csv file
f = open('output.csv')
csv_file = csv.reader(f)
#Loop through the CSV and create 2 lists, one with the static data and one with the position report
for row in csv_file:
    if row[8] == n:
      mmsil.append(row)
    else:
        csvl.append(row)
#Loop through the static data and check with the mmsi with the position reports and pushes the static data onto it
for y in mmsil:
    mmsi = y[0]
    for x in csvl:
        if x[0] == y[0]:
           x[6] = y[6]
           x[7] = y[7]
           x[10] = y[10]
           x[11] = y[11]
           x[12] = y[12]
           x[13] = y[13]
#Creates the output csv file
with open('clean1.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(csvl)           
           
            
            
