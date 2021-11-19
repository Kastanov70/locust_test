import time
import random
from locust import HttpUser, task, between


class MsisdnNumbers:
    msisdn_list = []
    index_of_list = 0

    def __init__(self):
        with open('msisdn.txt', 'r') as f:
            for line in f:
                self.msisdn_list.append("8901" + line[4:-1])

    def get_msisdn(self):
        msisdn = self.msisdn_list[self.index_of_list]
        if len(self.msisdn_list) == self.index_of_list:
            self.index_of_list = 0
        else:
            self.index_of_list = self.index_of_list + 1
        return msisdn


class QuickstartUser(HttpUser):
    wait_time = between(0.1, 0.4)

    # msisdn_object = None

    # def on_start(self):
    # self.msisdn_object = MsisdnNumbers()

    @task(1)
    def from_other_operators(self):

        headers = {
            'accept': 'text/xml; charset=utf-8',
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36",
            'Content-Type': 'text/xml'
        }
        with self.client.get("/t2_px.jpeg", catch_response=True, headers=headers,
                             name="/from_other_operators") as response:
            if response.status_code != 200:
                response.failure("Request failure!")
            elif response.cookies.keys()[0] != 'cookieparameters':
                response.failure("No 'cookieparameters' received!")
            elif response.elapsed.total_seconds() > 2:
                response.failure("Request took longer then 2s!")
            else:
                response.success()

    @task(1)
    def from_tele2_old(self):

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

        with self.client.get("/t2_px.jpeg", catch_response=True, headers=headers, name="/from_tele2_old") as response:
            if response.status_code != 200:
                response.failure("Request failure!")
            elif response.cookies.keys()[0] != 'cookieparameters':
                response.failure("No 'cookieparameters' received!")
            elif response.elapsed.total_seconds() > 2:
                response.failure("Request took longer then 2s!")
            else:
                response.success()

    @task(100)
    def from_tele2_new(self):

        headers = {"Host": "clid.tele2.ru", "X-Request-ID": "8098892511a4c0c7ceb734539a27862a",
                   "X-Real-IP": "176.59.52.56", "X-Forwarded-For": "176.59.52.56", "X-Forwarded-Host": "clid.tele2.ru",
                   "X-Forwarded-Port": "80", "X-Forwarded-Proto": "http", "X-Scheme": "http", "Save-Data": "on",
                   "Upgrade-Insecure-Requests": "1",
                   "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                   "Accept-Encoding": "gzip, deflate", "Accept-Language": "ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7",
                   "X-MSISDN": ('88' + str(random.randint(100000000, 999999999))), "X-IMSI": str(random.randint(100000000000000, 999999999999999))}

        with self.client.get("/t2_px.jpeg", catch_response=True, headers=headers, name="/from_tele2_new") as response:
            if response.status_code != 200:
                response.failure("Request failure!")
            elif response.cookies.keys()[0] != 'cookieparameters':
                response.failure("No 'cookieparameters' received!")
            elif response.elapsed.total_seconds() > 2:
                response.failure("Request took longer then 2s!")
            else:
                print(headers)
                print(response.headers)
                response.success()
