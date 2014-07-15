###  Created by Alison, Y.Y Wang

import csv

#--------------------------------------------------------------------#
### CSV ###
#--------------------------------------------------------------------#

### Read ###

# Way 1
data = []
with open("csvfile.csv","rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

# Way 2
data =[]
csvfile = open("csvfile.csv","rb")
reader = csvreader(csvfile)

csvfile.close()


### Write ###
# Way 1

def write_to_csv(outputname,mylist):
    with open(outputname+'.csv','wb')  as csvfile:
        writer = csv.writer(csvfile,
                            delimeter = ",",
                            quoting = csv.QUOTE_ALL)   # to quote all field. See also quote_none/quote_nonnumeric/quote_mininal
        
        header = ['Date','Year','sic-code','open','high','low','close']
        writer.writerow(header)     
        for row in mylist:          
            writer.writerow(row)        # Write row one at a time

# Way 2

csvfile = open("csvfile.csv","wb")
writer = csv.writer(csvfile)
writer.wirterows[wholelist]             # Write all rows at once
csvfile.close()

#--------------------------------------------------------------------#
### Text file###
#--------------------------------------------------------------------#

### Write ###
with open('txtfile.txt','wb') as text_file:
    for line in myList:
        for item in line:
            text_file.writelines(item.encode('utf8', 'replace')+'\t')
        text_file.write('\n')

#--------------------------------------------------------------------#
### MS Excel   ###
#--------------------------------------------------------------------#



