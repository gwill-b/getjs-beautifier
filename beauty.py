#!/usr/bin/python
from sys import argv
import jsbeautifier
import os
import requests
requests.packages.urllib3.disable_warnings() 
script, urls = argv

def main(jsurls):
    jspath = os.getcwd()+'/jsbeautified'
    os.mkdir(jspath)
    jsurls = open(jsurls, 'r')
    for url in jsurls:
        url = url.rstrip()
        if ".js" in url:
            try:
                save = open(jspath+"/"+url.split('/')[-1], 'w')
            except Exception as e:
                continue
            try:
                req = requests.get(url,verify=False, timeout=2, allow_redirects= False)
                beautify = jsbeautifier.beautify(req.content.decode())
                print(f'#==> {url}')
            except Exception as f:
                print("[-] something went wrong with requesting the link [-]\n"+str(f))
            save.write(beautify)
            save.close()
        else:
            continue
        

main(urls)
