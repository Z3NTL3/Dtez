# Importing basic libs
import httpx
import sys
import random
from time import strftime
import datetime
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import Future
from concurrent.futures import as_completed
# end basic libs

# Run this script on your local internet wifi do not use vpn or proxies
'''
Programmed by Z3NTL3 (Efdal)
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

    if cms == CMS[1]:
        with open("wordpress.txt",'a+')as f:
            f.write(f'{CURRENT_TIME} URL: {sitename}')
    elif cms == CMS[2]:
        with open("xenforo.txt",'a+')as f:
            f.write(f'{CURRENT_TIME} URL: {sitename}')
    elif cms == CMS[3]:
        with open("mybb.txt",'a+')as f:
            f.write(f'{CURRENT_TIME} URL: {sitename}')
    detects += 1

def urlget(urllist):
    global undetected, amount_sites,connection_errors
    urls = urllist
    
    try:
        with httpx.Client(http2=True,headers=HEADER,timeout=15) as client:
            req = client.get(urllist)
            res = req.text
        
        if req.status_code >= 500 and req.status_code < 600 or req.status_code >= 400 and req.status_code <= 499:
            print(f"\n\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Undetected CMS: '\033[38;5;200m{urls}\033[32m\' \033[31mConnection Error\033[0m")
            undetected += 1
        else:
            if 'wp-content/themes' in res:
                # WordPress
                log(urllist, CMS[1])
                print(f"\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Detected CMS: \033[32m\'\033[38;5;200mWordPress\033[32m\'\033[0m on \033[32m\'\033[38;5;200m{urls}\033[32m\'\033[0m")
                amount_sites += 1

            elif 'Xenforo' in res or 'XenForo' in res or 'xenforo' in res:
                # XenForo
                log(urllist, CMS[2])
                print(f"\n\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Detected CMS: \033[32m\'\033[38;5;200mXenForo\033[32m\'\033[0m on \033[32m\'\033[38;5;200m{urls}\033[32m\'\033[0m") 
                amount_sites += 1
            elif 'MyBB' in res or 'mybb' in res or 'myBB' in res:
                # MyBB
                log(urllist, CMS[3])
                print(f"\n\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Detected CMS: \033[32m\'\033[38;5;200mMyBB\033[32m\'\033[0m on \033[32m\'\033[38;5;200m{urls}\033[32m\'\033[0m")
                amount_sites += 1
            
            else:
                print(f"\n\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Undetected CMS: '\033[38;5;200m{urls}\033[32m\'\033[0m")
                undetected += 1
      
    except:
        print(f"\n\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Undetected CMS: '\033[38;5;200m{urls}\033[32m\' \033[31mConnection Error\033[0m")
        connection_errors += 1
    


def Main():
    print(LOGO)
    if Loaded() < 1:
        sys.exit(f"\033[38;5;200m[\033[38;5;195mDATA\033[38;5;200m]\033[0m\n\t\033[31mMinimum 1 site to check in \033[32m\'sites.txt\'\033[0m\n")
    else:
        pass
    urls = URLS()
    pool = ThreadPoolExecutor(max_workers=61)
    print(f"\n\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}Checking has been started for \033[38;5;200m{len(URLS())}\033[0m \033[34msites\033[0m\n")
    futures = [pool.submit(urlget,url) for url in urls]

    ftrs = []
    for future in as_completed(futures):
        ftrs.append(future)
    pool.shutdown()

    ths = []
    for f in ftrs:
        if f.done():
            ths.append('yes')
    if len(ths) == len(ftrs):
        print(f"\n\033[38;5;200m[\033[38;5;198mSYSTEM\033[38;5;200m] \033[0m{CURRENT_TIME}: {NEWLINE}\033[32mThreads Terminated Because the process is completed\033[0m\n")
    
if __name__ == '__main__':
    Main()
