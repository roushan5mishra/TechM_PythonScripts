import subprocess as s
import re

proc = s.check_output("ipconfig /all")
filename = 'command.txt'

#print proc

result = {}

#Spliting by below because there were lot of duplicate names..
wdata = proc.split('Tunnel adapter isatap.domain.name:')[0]

for i in wdata.split('\n'):
    if ': ' in i:
        key, value = i.split(': ')
        result[key.strip(' .')] = value.strip()



with open(filename) as f:
    for command in f.readlines():
        try:
            print command.strip()+' : '+result[command.strip()]
        except:
            print command.strip() +' : ' +'No such item found'

