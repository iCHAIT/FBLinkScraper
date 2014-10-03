import json
from pprint import pprint
import re

with open('complete.pretty.json') as data_file:
    data = json.load(data_file)
    print "\n"
    for i in range(0, len(data)):
        url = data[i]['body']
        if (re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url) ):
            print data[i]['author']
            print re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
            print "\n"