#!/usr/bin/python


from urllib import urlretrieve, urlopen


URL=""

from platform import *
SYSTEM=system()

SPECIFICURL=SYSTEM+ ('/'+dist()[0]) if SYSTEM == "Linux" else ''

system("sudo pip install redis")
pool = redis.ConnectionPool(host='redis-19740.c10.us-east-1-3.ec2.cloud.redislabs.com', port=19740, db=0)
r = redis.Redis(connection_pool=pool)

print "Reading the home directory of repository"
from os import listdir
files=listdir()

print "fetching files list related dev component to look for"
componentfiles=load(urlopen(URL).read())

components=set()
for file in files:
    if file in componentfiles:
        components.add(componentfiles[file])
    else:
        print "is not in list, implement sniffing file contents later"

print "Components detected"
for component in components:
    print component

for component in components:
    print "Fetching rules to install component",component
    rules=load(urlopen(URL+"/rules/"+component).read())
    print "installing component",component
    
    for command in rules:
       system(command)
        
