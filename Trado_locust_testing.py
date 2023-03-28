import random

from locust import HttpUser, constant, task, SequentialTaskSet
from Project_folder.pages.common_page import Commons


class MyReqRes(SequentialTaskSet):

    @task
    def create_user(self):
        res = self.client.post(
            {"phone": f"{Commons.random_phone_number()}",
             "policy": 'true',
             "marketingList": 'false',
             "bnNumber": f"{random.randrange(30, 90)}",
             "register": 'true',
             "type": "phone",
             "info": {"lng": "hebrew",
                      "platform": "web",
                      "screenHeight": 864,
                      "screenWidth": 1536,
                      "location": {"href": "https://qa.trado.co.il/",
                                   "origin": "https://qa.trado.co.il",
                                   "protocol": "https:",
                                   "host": "qa.trado.co.il",
                                   "hostname": "qa.trado.co.il",
                                   "port": "",
                                   "pathname": "/",
                                   "search": "",
                                   "hash": ""}}}
        )
        # @task
    # def post_status(self):
    #     res = self.client.post("/?status=success")
    #     print("Post Method Status is", res.status_code)


class MySeqTest(HttpUser):
    wait_time = constant(1)
    host = "https://qa.trado.co.il/"

    tasks = [MyReqRes]
