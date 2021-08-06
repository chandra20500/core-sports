import pandas as pd
import requests
from requests.api import request
from login import Auth
import json
from import_schema import post_script, put_script, put_obj_names


class Staging(Auth):
    def __init__(self):
        super()

    def CreateSchema(self, body, cred, url):
        print("== start ==")
        api_header = self.StagingLogin(cred)
        r = requests.post(url = schema_url,json = body, headers = api_header)
        print("== done ==")
        print(r.text)

    def AddRelation(self, body, cred, put_url, obj_name):
        print("== start ==")
        api_header = self.StagingLogin(cred)
        r = requests.put(url = put_url + '/' + obj_name,json = body, headers = api_header)
        print("== done ==")
        print(put_url + '/' + obj_name)
        print(r.text)

schema_url = 'https://maverick-core-platform-objects-api-staging.dev.core.maverick.io/v1/tenants/core_sports/custom-schema'
Login_cred = {
        "loginId": "core.sports@core_sports.mavq.io",
        "password": "Core_Sports123"
    }

staging = Staging()
for i in post_script:
    print(staging.CreateSchema(i, Login_cred, schema_url))
for i in range (1,len(put_obj_names)):
    print(staging.AddRelation(put_script[i], Login_cred, schema_url, put_obj_names[i]))