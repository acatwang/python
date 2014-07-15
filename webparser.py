###  Created by Alison, Y.Y Wang

from BeautifulSoup import BeautifulSoup
import json, urllib2
import re

#--------------------------------------------------------------------#
### Usage of urlib2 ###
#--------------------------------------------------------------------#
req=urllib2.urlopen("http://www.imsdb.com/scripts/Godfather.html") #fetch html page

print req
print req.code
print req.geturl()
print req.info()
print req.read()

### JSON
json_str = '{"A": 1, "B": 2, "C": [1, 2]}'
d = json.loads(json_str)
print d
print d['C'][0]

#--------------------------------------------------------------------#
### Basic text parser and RegEx ###
#--------------------------------------------------------------------#

### Useful trick ###

s = "Some (messy) String "
text = s[.find(".")+1:]                 # s.find return the first index where substring is found  
text = s[s.find("(")+1:s.find(")")]     # get text between parenthesis
text = s[1:-1]                          # alternative way to get text between something

text = s.strip["."]                     # remove leading and trailing dot. Also check s.lstrip and s.rstrip.
text = s.replace(","," ")               # replace comma by space

split_by_comma = s.split[","]
split_by_tab = s.split["\t"]
split_by_line = s.split["\n"]
split_by_line2 = s.splitlines(True)     # ['Line1\n','Line2\n']


### RegEx ###

# re.search(pattern,string)# 

matchOrNot = re.search(r'(GET|POST)\shttps?://\D+', myString)
# Check if http followed either GET or POST and followed by NON-digit(\D) charactoer
# https? - there may be zero or more s
# \D+    - at least one non-digit char
      
match = re.search(r"(\d+?/Mar/2004).*?(http.+?)\.(\w+)(?:/|:|\s|\")+(.*)", myString)
# Use Parentheses to create group 
allString = match.gorup()
date = match.group(1)
domain = match.group(3)


# re.findall #

mailLIst = re.findall(r'[\w\.-]+@[\w\.-]', myString)        # return a list of ALL matches in the string. 

emails = re.findall(r'([\w\.-]+)@([\w\.-])', myString)      # Use Parentheses to create group 
email[0] = ('username','google.com')                        # return a Tuple


#--------------------------------------------------------------------#
### Usage of Beautiful Soup                ###
### parse html page in a strcutured format ###
### Doc:                                   ###
#--------------------------------------------------------------------#

soup = BeautifulSoup(req)               # feed a html page to the soup
soup.prettify()                         # return parsed tree
    
print type(soup.body.p)

first_p_tag = soup.p

get_attribute = soup.p['class']

get_text = soup.p.string

parent_tag =  soup.p.parent.name

list_of_p_tag = soup.findAll('p')       # format: beautiful soup tag

list_of_two_tag = soup.findAll(['p','li']) 

find_by_argument = soup.find(id="LookforthisID")

