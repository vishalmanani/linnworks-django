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

        my_token = json.loads(response.text)
        print("mytoken=====>", my_token)
        print("Token=====>", my_token.get('Token'))
        main_token = my_token.get('Token')
        location_url = "https://eu-ext.linnworks.net//api/Inventory/GetCategories"
        # l_payload = {
        #     "includeDeleted": "true",
        #     "includeArchived": "true",
        # }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Authorization': main_token,
        }
        location = requests.post(location_url, headers=headers)
        print("location_code===>", location.status_code)
        print("location_text===>", location.text)

        return render(request, self.template, locals())