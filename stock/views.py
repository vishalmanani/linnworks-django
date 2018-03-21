import json

from django.shortcuts import render
from django.views import View
import requests


class AuthToken(View):
    template = 'index.html'

    def get(self, request):
        print("call get method")
        token = request.GET.get('token', None)
        print("token=======>", token)

        url = 'https://api.linnworks.net//api/Auth/AuthorizeByApplication'
        payload = {
            "applicationId": "65625950-d006-4e8f-a5a4-b3c8e1ca4cfe",
            "applicationSecret": "8f0df2ed-9338-402b-9dd8-4b3efa560d0e",
            "token": token,
        }
        response = requests.post(url, data=payload)

        print("status_code====>", response.status_code)
        print("status_text====>", response.text)

        location_url = "https://eu-ext.linnworks.net//api/Locations/GetLocation"
        l_payload = {
            "pkStockLocationId": "63d2d7b6-ec58-4f2c-a55e-2f8be11ea296",
        }
        headers = {
            'Host': 'eu - ext.linnworks.net',
            'Connection': 'keep - alive',
            'Accept': 'application / json, text / javascript, * / *; q = 0.01',
            'Origin': 'https:// www.linnworks.net',
            'Accept-Language': 'en',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
            'Content-Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
            'Referer': 'https: // www.linnworks.net /',
            'Accept-Encoding': 'gzip, deflate',
            'Authorization': token,
        }
        location = requests.post(location_url, data=json.dumps(l_payload), headers=headers)
        print("location_code===>", location.status_code)
        print("location_text===>", location.text)

        return render(request, self.template, locals())