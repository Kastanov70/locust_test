from locust import HttpUser, task, between
import random

# https://clid.tele2.ru/kafka

class QuickstartUser(HttpUser):
    wait_time = between(0.1, 0.4)

    @task
    def from_other_operators(self):

        headers = {
            'accept': 'text/xml; charset=utf-8',
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.50 Mobile Safari/537.36",
            'Content-Type': 'text/xml'
        }
        with self.client.get("/test", catch_response=True, headers=headers,
                             name="/mongo") as response:
            if response.status_code != 204:
                response.failure("Request failure!")
            # elif response.cookies.keys()[0] != 'cookieparameters':
            #     response.failure("No 'cookieparameters' received!")
            elif response.elapsed.total_seconds() > 2:
                response.failure("Request took longer then 2s!")
            else:
                response.success()
