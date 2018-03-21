from django.shortcuts import render
from django.views import View
import requests
from django.http import JsonResponse


class AuthToken(View):
    template = 'index.html'

    def get(self, request):
        print("call get method")
        token = request.GET.get('token', None)
        print("token=======>", token)

        url = 'https://api.linnworks.net//api/Auth/AuthorizeByApplication'
        payload = {
            'applicationId': '8d9172f1-9fe0-4394-95ee-25495e35d89f',
            'applicationSecret': '8af5f1fb-b384-42da-86c8-667132cf2349',
            'token': token
        }
        response = requests.post(url, data=payload)
        print("====>", response)
        print("status_code====>", response.status_code)
        print("status_code====>", response.text)
        print("====>", dir(response))

        return render(request, self.template, locals())

    def post(self, request):
        url = 'https://api.linnworks.net//api/Auth/AuthorizeByApplication'
        payload = {
            'applicationId': '8d9172f1-9fe0-4394-95ee-25495e35d89f',
            'applicationSecret': '8af5f1fb-b384-42da-86c8-667132cf2349',
            'token': '1d8993875b980f035df7f71c6afac8eb'
        }
        data = requests.post(url, data=payload)
        print("====>", data)
        response = {'status': '200'}
        return JsonResponse(response)
