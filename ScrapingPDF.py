import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL you want to scrap:- ")  
# For Testing enter https://doc.lagout.org/programmation/python/ in url
pwd = input("Enter where to store : Example:'/home/yash/' include forward slahes too: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
list_site = list()
tags = soup('a')
list_name = list()

for tag in tags:
    print(tag)
    if(re.findall('\.pdf$',str(tag.get('href',None)))):
        list_site.append(url+str(tag.get('href',None)))
        #list_site.append(str(tag.get('href',None)))  # If above line is not working comment it out and remove # from this line..
        list_name.append(tag.contents[0])
var=""
count = int(1)
for l,n in zip(list_site,list_name):
    var = pwd+n
    response = urllib.request.urlopen(l)
    file = open(var,'wb')
    print(count,' File Done..')
    count+=1
    file.write(response.read())
    file.close()
