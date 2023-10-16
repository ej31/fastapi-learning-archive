import requests

_header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Teamcode": "XX",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Access-Control-Allow-Methods":  "GET, PUT, POST, DELETE, OPTIONS",
    "Access-Control-Allow-Origin": "*",
    "Cache-Control": "no-cache",
    "Origin": "https://www.kbl.or.kr",
    "Channel": "WEB"
}

if __name__ == '__main__':
    _resp = requests.get("https://api.kbl.or.kr/matches?fromDate=20230201&toDate=20230228&tcodeList=all&favStat=false",
                         headers=_header)
    print(_resp.json())
