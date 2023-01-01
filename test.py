import requests
try:

    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        
    resp:requests.Response = requests.get('https://oss.v2rayse.com/proxies/data/2022-10-25/1M83g8.yaml',headers=headers, verify=False, timeout=10)
    if resp.status_code != 200:
        print(f'[!] Got HTTP Status Code {resp.status_code}')
        
    print(resp.text)
except Exception as e:
        print(e)
