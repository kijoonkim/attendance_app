import requests, json, os
from dotenv import load_dotenv
import getmac, socket

def call_attendance():
    host = os.getenv('host')
    cmd = os.getenv('cmd')
    headers = {'Content-Type': 'application/json; chearset=utf-8'}
    params = {'mac':getmac.get_mac_address(), 'ip':socket.gethostbyname(socket.gethostname())}
    print(f'params = {params}')
    print(f'address = {host}/{cmd}')
    res = requests.post(host+'/'+cmd, data=json.dumps(params), headers=headers)

    print(str(res) + " | " + res.text)

if __name__ == "__main__":
    # .env 파일 로드
    load_dotenv()
    BASE_DIR = os.getcwd()
    call_attendance()
