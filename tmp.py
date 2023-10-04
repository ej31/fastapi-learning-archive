import requests


with requests.session() as req:
    resp = req.get("https://ko.dict.naver.com/#/search?query=호수")
    req.cookies = resp.cookies
    resp2 = req.get("https://ko.dict.naver.com/api3/koko/search?query=%ED%98%B8%EC%88%98&m=pc&lang=ko")
    print(resp2)

resp = requests.get("https://ko.dict.naver.com/#/search?query=호수")
print(resp)
