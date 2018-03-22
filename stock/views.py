import json

from django.shortcuts import render
from django.views import View
import requests
from .models import Token

class AuthToken(View):
    template = 'index.html'

    def get(self, request):
        token = request.GET.get('token', None)
        print("token=======>", token)

        url = 'https://api.linnworks.net//api/Auth/AuthorizeByApplication'
        payload = {
            "applicationId": "65625950-d006-4e8f-a5a4-b3c8e1ca4cfe",
            "applicationSecret": "8f0df2ed-9338-402b-9dd8-4b3efa560d0e",
            "token": token,
        }
        response = requests.post(url, data=payload)

        print("AuthorizeByApplication status_code====>", response.status_code)
        print("AuthorizeByApplication status_text====>", response.text)

        my_token = json.loads(response.text)
        main_token = my_token.get('Token')

        Token.objects.create(token=main_token)

        return render(request, self.template, locals())


class TestApi(View):
    template = 'index.html'

    def get(self, request):
        main_token = Token.objects.last()
        print("main_token last===>", main_token.token)
        location_url = "https://eu-ext.linnworks.net//api/Inventory/GetPackageGroups"
        # l_payload = {
        #     "stockItemId": "ceb6c502-54c4-4ca9-b9cb-5d1131a309da",
        #     "locationId": "ed65daa9-2867-4d05-b30f-3868b469a7e6",
        #     "startDate": "2018-02-19T16:57:06.0303122+00:00",
        #     "endDate": "2018-02-19T16:57:06.0358278+00:00"
        # }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Authorization': main_token.token,
        }
        location = requests.post(location_url, headers=headers)
        print("location_code===>", location.status_code)
        print("location_text===>", location.text)

        return render(request, self.template, locals())
