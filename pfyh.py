import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
url1 = 'https://per.spdb.com.cn/bank_financing/financial_product/'

session = requests.Session()

session.get(url1, headers=headers)
time.sleep(2)

url2 = 'https://per.spdb.com.cn/was5/web/search'

data = {
    "metadata": "finance_state|finance_no|finance_allname|finance_anticipate_rate|finance_limittime|finance_lmttime_info|finance_type|docpuburl|finance_ipo_enddate|finance_indi_ipominamnt|finance_indi_applminamnt|finance_risklevel|product_attr|finance_ipoapp_flag|finance_next_openday",
    "channelid": 266906,
    "page": 1,
    "searchword": "(product_type=3)*finance_limittime = %*(finance_currency = 01)*(finance_state='可购买')"
}
res = session.post(url2, headers=headers, data=data)
print(res.content)