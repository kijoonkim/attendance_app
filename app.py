import requests, json, os
from dotenv import load_dotenv
import getmac, socket

def call_attendance():
    host = os.getenv('host')
    path = os.getenv('path')
    headers = {'Content-Type': 'application/json; chearset=utf-8'}
    params = {'mac':getmac.get_mac_address(), 'ip':socket.gethostbyname(socket.gethostname())}
    print(f'params = {params}')
    print(f'address = {host+'/'+path}')
    res = requests.post(host+'/'+path, data=json.dumps(params), headers=headers)

    print(str(res) + " | " + res.text)

if __name__ == "__main__":
    # .env 파일 로드
    load_dotenv()
    BASE_DIR = os.getcwd()
    call_attendance()
