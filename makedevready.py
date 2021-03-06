#!/usr/bin/python


from urllib import urlretrieve, urlopen


URL="https://s3.amazonaws.com/ntadiko/makedevready/"

# Package manager identification code
PACKAGE_MANAGER="apt-get"

print "Reading the home directory of repository"
from os import listdir
files=listdir()

print "fetching files list related dev component to look for"
componentfiles=load(urlopen(URL+"/componentfiles").read())

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
    rules=load(urlopen(URL+"/rules/"+component+'/'+PACKAGE_MANAGER).read())
    print "installing component",component
    
    for command in rules:
       system(command)
        
