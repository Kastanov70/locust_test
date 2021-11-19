headers = {
    "Host": "clid.tele2.ru",
    "X-Request-ID": "8098892511a4c0c7ceb734539a27862a",
    "X-Real-IP": "176.59.52.56",
    "X-Forwarded-For": "176.59.52.56",
    "X-Forwarded-Host": "clid.tele2.ru",
    "X-Forwarded-Port": "80",
    "X-Forwarded-Proto": "http",
    "X-Scheme": "http",
    "Save-Data": "on",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7",
    "Cookie": "cookieparameters=\"eyJmaW5pdF9pZCI6ICIyNTk1OWI5Ny02MDA4LTQxNjUtOTk1ZS1iYzMzMzA5Y2M4MTEiLCAidGltZXN0YW1wIjogMTYzNTg3MTE3OSwgImNyeXB0b3RyaXBsZXQiOiAiTFZ5Um9HZStMMmpldlZ0K2dtU1IrQT09LjlUemZkQ29MaGdUSXNWem4vQjZ1NVE9PS5YcEw2Nkx3UHJ5MHpBd21RZnd4Q2h5bkNST25GZUpWMTNIZ1VKVDNtK1FWRzZwYVFXRHJNaFY5MjZ1QTU3b0gzUCtzSUNRU0NMcUVXaERWdXJvVENrNTdGIn0=\"",
    "X-MSISDN": "79013309803",
    "X-IMSI": "250207440754568"
}


class MsisdnNumbers:
    msisdn_list = []
    index_of_list = 0

    def __init__(self):
        with open('msisdn.txt', 'r') as f:
            for line in f:
                self.msisdn_list.append("8800" + line[4:-1])

    def get_msisdn(self):
        msisdn = self.msisdn_list[self.index_of_list]
        if len(self.msisdn_list) == self.index_of_list:
            self.index_of_list = 0
        else:
            self.index_of_list = self.index_of_list + 1
        return msisdn


msisdn_object = MsisdnNumbers()
print(headers["X-MSISDN"])
headers["X-MSISDN"] = msisdn_object.get_msisdn()
print(headers)
headers["X-MSISDN"] = msisdn_object.get_msisdn()
print(headers)
headers["X-MSISDN"] = msisdn_object.get_msisdn()
print(headers)
headers["X-MSISDN"] = msisdn_object.get_msisdn()
print(headers)

