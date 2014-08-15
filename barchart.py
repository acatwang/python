__author__ = 'Alison'
### Created by Alison Wang 2014.06.13

### How to use this script:
### 1. To parse historical data, go to http://www.barchart.com/stocks/sectors/sic/
### 2. Select the industry of interest and copy the web addr to the variable "webaddr"
### 3. Type in the output file name at "outputname)
### 4. Click F5 or run the script


from BeautifulSoup import BeautifulSoup
import json, urllib2
import re
import csv

# Copy and paste the link below
webaddr = "http://www.barchart.com/stocks/sectors/sic/-004C"

# Type desired output file name here
outputname = "stock0815"



def parse_data(link):
    
    ### Fetch html page using urllib2
    req=urllib2.urlopen(link)
    soup1 = BeautifulSoup(req)
    hist_data = (soup1.findAll('area'))
    
    
    ### Parse the data    
    output_list=[]
    
    for i in range(len(hist_data)):
        s = hist_data[i]['onmousemove']                 # select specific attr within beautifulsoup tag
        txt = s[s.find("(")+1:s.find(")")]              #return text between parenthesis
        numbers=txt.split(', ')  
        for j in range(4,len(numbers)):
            numbers[j] = numbers[j][1:-1]               # transform quote into numeric data
        numbers[2]=numbers[2][numbers[2].find(".")+1:]  # Fetch date part
        numbers[3]=numbers[3][0:-2]                     # strip the quote mark
  
        output_list.extend([numbers[2:]])
    
    return output_list


### Write into CSV

def write_to_csv(outputname,mylist):
    with open(outputname+'.csv','wb')  as csvfile:
          writer = csv.writer(csvfile)
          header = ['Date','Year','sic-code','open','high','low','close']
          writer.writerow(header)
          for row in mylist:
              if len(row)>5:
                  writer.writerow(row)



mylist = parse_data(webaddr)
write_to_csv(outputfile, mylist)

