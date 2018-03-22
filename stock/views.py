import json

from django.shortcuts import render
from django.views import View
import requests

main_token = None


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

        my_token = json.loads(response.text)
        main_token = my_token.get('Token')

        return render(request, self.template, locals())


class TestApi(View):
    template = 'index.html'

    def get(self, request):
        print("main_token===>", main_token)
        location_url = "https://eu-ext.linnworks.net//api/Stock/GetStockConsumption"
        l_payload = {
            "stockItemId": "ceb6c502-54c4-4ca9-b9cb-5d1131a309da",
            "locationId": "ed65daa9-2867-4d05-b30f-3868b469a7e6",
            "startDate": "2018-02-19T16:57:06.0303122+00:00",
            "endDate": "2018-02-19T16:57:06.0358278+00:00"
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Authorization': main_token,
        }
        location = requests.post(location_url, data=json.dumps(l_payload), headers=headers)
        print("location_code===>", location.status_code)
        print("location_text===>", location.text)

        return render(request, self.template, locals())
