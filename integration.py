import pandas as pd
import requests
from requests.api import request
from login import Auth
import json
from import_schema import post_script, put_script, put_obj_names


class Integration(Auth):
    def __init__(self):
        super()

    def CreateSchema(self, body, cred, url):
        print("== start ==")
        api_header = self.IntegrationLogin(cred)
        print(api_header)
        r = requests.post(url = schema_url,json = body, headers = api_header)
        print("== done ==")
        print(r.text)

    def AddRelation(self, body, cred, put_url, obj_name):
        print("== start ==")
        api_header = self.IntegrationLogin(cred)
        r = requests.put(url = put_url + '/' + obj_name,json = body, headers = api_header)
        print("== done ==")
        print(put_url + '/' + obj_name)
        print(r.text)

schema_url = 'https://objects-api.mavq.io/v1/tenants/core-sports-dev/custom-schema'
Login_cred = {
    "loginId":"rajan.panigrahi+core-sports-dev-2@mavq.com",
    "password":"PR@J6Vc*4fiE",
    "applicationId":"e4c5384e-6c94-4761-acad-a1328509b1da"
}

staging = Integration()

# for i in post_script:
#     print(staging.CreateSchema(i, Login_cred, schema_url))
for i in range (1,len(put_obj_names)):
    print(staging.AddRelation(put_script[i], Login_cred, schema_url, put_obj_names[i]))