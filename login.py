import pandas as pd
import numpy as np
import requests
import datetime
import json
import random

from requests import api

class Auth:
    def StagingLogin(self, admin_login_body):
        admin_url = 'https://fusion.labs.mtxb2b.com/api/login'
        response = requests.post(url = admin_url, json = admin_login_body, headers='')
        x = response.json()
        ADMIN_TOKEN = x['token']
        
        Login_url = 'https://maverick-core-platform-core-api-staging.dev.core.maverick.io/auth/external_service_with_jwt/login'
        
        hed = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
        login_response = requests.post(url = Login_url, json = {}, headers=hed)

        y = login_response.json()
        ADMIN_ACCESS_TOKEN = y['access_token']
        # header for all API's
        api_header = {'Authorization': 'Bearer ' + ADMIN_ACCESS_TOKEN}
        return api_header

    def IntegrationLogin(self, admin_login_body):
        admin_url = 'https://auth.mavq.io/api/login'
        response = requests.post(url = admin_url, json = admin_login_body, headers='')
        x = response.json()
        ADMIN_TOKEN = x['token']
        
        Login_url = 'https://core-api.mavq.io/auth/external_service_with_jwt/login'
        
        hed = {'Authorization': 'Bearer ' + ADMIN_TOKEN}
        login_response = requests.post(url = Login_url, json = {}, headers=hed)

        y = login_response.json()
        ADMIN_ACCESS_TOKEN = y['access_token']
        # header for all API's
        api_header = {'Authorization': 'Bearer ' + ADMIN_ACCESS_TOKEN}
        return api_header