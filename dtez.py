# Importing basic libs
import requests
import sys
from threading import Thread
import random
from time import strftime
import datetime
# end basic libs

# Run this script on your local internet wifi do not use vpn or proxies
'''
Programmed by Z3NTL3 (Efdal)
z3ntl3.github.io

README

SUPPORTED CMS TYPES:
Wordpress
Xenforo
MYBB

This tool may be used subject to the following conditions.

- Don't change anything in the source
- Do not copy and paste content
- Mention credits to the creator (Z3NTL3)
- Don't sell it
'''


# Global and constant variables
LOGO = """
     \033[38;5;198m·▄▄▄▄  ▄▄▄▄▄▄▄▄ .·▄▄▄▄•
     \033[38;5;199m██▪ ██ •██  ▀▄.▀·▪▀·.█▌
     \033[38;5;198m▐█· ▐█▌ ▐█.▪▐▀▀▪▄▄█▀▀▀•
     \033[38;5;201m██. ██  ▐█▌·▐█▄▄▌█▌▪▄█▀
     \033[38;5;200m▀▀▀▀▀•  ▀▀▀  ▀▀▀ ·▀▀▀ •\033[0m
      \033[1m\033[38;5;200mMulti\033[38;5;201mple C\033[38;5;198mMS De\033[38;5;199mtector\033[0m
       \033[38;5;200m[ \033[38;5;1m\033[1mz3ntl3.github.io \033[38;5;200m]\033[0m
         \033[1m\033[38;5;198m@\033[1m\033[38;5;200mZ3NTL3 \033[1m\033[38;5;201m(\033[1m\033[38;5;198mEfdal\033[1m\033[38;5;201m)\033[0m
"""
HEADER = {
    'Connection': 'keep-alive',
    'cache-control': 'no-cache'
}
CURRENT_TIME = strftime("[%D] %H:%M:%S")
NEWLINE = '\n'

CMS = {
    1 : 'WordPress',
    2: 'XenForo',
    3: 'MyBB'
}


# end global variables

detects = 0
undetected = 0
amount_sites = 0
connection_errors = 0


def Loaded():
    with open('sites.txt','r')as f:
        data = f.read().strip(' ').split('\n')
    
    return len(data)

def URLS():
    query  = [
        'http://', 
        'https://'
    ]
    with open('sites.txt','r')as f:
        data = f.read().strip(' ').split('\n')
        
    for q in query:
        if q in data:
            sys.exit('[Err]\nPlease put only http://urls.com or https://urls.com in \'proxies.txt\'')
        else:
            pass
    return data

def log(sitename,cms):
    global detects

    with open("cms-detect.txt",'a+')as f:
        f.write(f'{CURRENT_TIME} URL: {sitename} |  CMS: {cms}{NEWLINE}')
        detects += 1

def urlget(*,urllist):
    print(f"\n\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Checking has been started for \033[38;5;200m{len(URLS())}\033[0m \033[34msites\033[0m\n")
    print()
    global undetected, amount_sites,connection_errors
    begin = datetime.datetime.now()
    
    for urls in urllist:
        try:
            req = requests.get(urls, headers=HEADER, timeout=15)
            res = req.content.decode('utf-8')
            if req.status_code == 200:
                if 'wp-content/themes' in res:
                    # WordPress
                    log(urls, CMS[1])
                    print(f"\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Detected CMS: \033[32m\'\033[38;5;200mWordPress\033[32m\'\033[0m on \033[32m\'\033[38;5;200m{urls}\033[32m\'\033[0m")
                    amount_sites += 1

                elif 'Xenforo' in res or 'XenForo' in res or 'xenforo' in res:
                    # XenForo
                    log(urls, CMS[2])
                    print(f"\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Detected CMS: \033[32m\'\033[38;5;200mXenForo\033[32m\'\033[0m on \033[32m\'\033[38;5;200m{urls}\033[32m\'\033[0m")
                    
                    amount_sites += 1
                elif 'MyBB' in res or 'mybb' in res or 'myBB' in res:
                    # MyBB
                    log(urls, CMS[3])
                    print(f"\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Detected CMS: \033[32m\'\033[38;5;200mMyBB\033[32m\'\033[0m on \033[32m\'\033[38;5;200m{urls}\033[32m\'\033[0m")
                    
                    amount_sites += 1
                
                else:
                    undetected += 1
            else:
                connection_errors += 1
        except:
            connection_errors += 1
    
    genomen_tijd = datetime.datetime.now() - begin
    print()
    print(f"\033[38;5;200m[\033[38;5;1mRESULTs\033[38;5;200m] \033[0m{CURRENT_TIME}:\nScanned \033[38;5;201m{Loaded()}\033[0m in \033[38;5;198m{genomen_tijd}\033[0m MS.") 
    print()
    print(f"\033[38;5;200m[\033[38;5;195mDATA\033[38;5;200m]\033[0m\n\t\033[38;5;195mAmount Sites Scanned: \033[38;5;200m{amount_sites}\n\t\033[38;5;195mDetections: \033[38;5;200m{detects}\n\t\033[38;5;195mUndetected: \033[38;5;200m{undetected}\n\t\033[38;5;195mConnection Errors: \033[38;5;200m{connection_errors}\n\t\033[38;5;195mSaved in: \033[32m\'\033[38;5;200mcms-detect.txt\033[32m\'\033[0m\n")   
    

     

if __name__ == '__main__':
    print(LOGO)
    if Loaded() < 1:
        sys.exit(f"\033[38;5;200m[\033[38;5;195mDATA\033[38;5;200m]\033[0m\n\t\033[31mMinimum 1 site to check in \033[32m\'sites.txt\'\033[0m\n")
    else:
        pass

    th = Thread(target=urlget(urllist=URLS()))
    th.daemon = True # making sure when tool exits thread also exit (0)
    th.start()
    th.join()
