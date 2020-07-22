import requests

session = requests.Session()

headers = {
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
url = 'https://item.taobao.com/item.htm?id=620420595440'
res = session.get(url=url, headers=headers)
print(res.text)

data = {"pageCode":"mainDetail",
        "ua":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "params":"{\"url\":\"https://h5.m.taobao.com/awp/core/detail.htm?id=620420595440\",\"referrer\":\"\",\"oneId\":null,\"isTBInstalled\":\"null\",\"fid\":\"dmOrDTNJXMo\"}"}