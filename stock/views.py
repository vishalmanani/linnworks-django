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
        location_url = "https://eu-ext.linnworks.net//api/Inventory/UpdateInventoryItem"
        # location_url = "https://eu-ext.linnworks.net//api/Stock/SetStockLevel"
        # location_url="https://eu-ext.linnworks.net//api/Inventory/GetCategories"
        # location_url="https://eu-ext.linnworks.net//api/Inventory/GetPackageGroups"
        # payload = dict(
        #     orderId='2843dbfd-eebf-45d4-8902-448e7422cb96',
        #     fulfilmentLocationId="2b79ae14-3145-4b1f-89a3-718eb377d49a",
        #     loadItems="true",
        #     loadAdditionalInfo="true",
        # )
        # payload = dict(
        #     update=json.dumps({
        #         "pkId": "911db59c-1da6-4c9f-b88f-6325a7e5c303",
        #         "fieldList": [
        #             {
        #                 "Key": "",
        #                 "Value": "50"
        #             }
        #         ]
        #     })
        # )

        # payload = dict(
        #     stockLevels=json.dumps([
        #         {
        #             "SKU": "A1001",
        #             "LocationId": "00000000-0000-0000-0000-000000000000",
        #             "InOrders": 10,
        #         }
        #     ]),
        # )

        payload = dict(

            inventoryItem=json.dumps({
                # "VariationGroupName": "sample string 1",
                "Quantity": 500,
                "InOrder": 200,
                "Due": 300,
                "MinimumLevel": 10,
                "Available": 10,
                "CreationDate": "2018-02-19T16:57:06.8269989+00:00",
                "IsCompositeParent": "true",
                "ItemNumber": "A1001",
                "ItemTitle": "sample string 6",
                "BarcodeNumber": "sample string 7",
                "MetaData": "sample string 8",
                "isBatchedStockType": "false",
                "PurchasePrice": 20,
                "RetailPrice": 20,
                "TaxRate": 10,
                "PostalServiceId": "00000000-0000-0000-0000-000000000000",
                "PostalServiceName": "Default",
                "CategoryId": "00000000-0000-0000-0000-000000000000",
                "CategoryName": "Default",
                "PackageGroupId": "00000000-0000-0000-0000-000000000000",
                "PackageGroupName": "Default",
                "Height": 17.1,
                "Width": 18.1,
                "Depth": 19.1,
                "Weight": 20.1,
                "InventoryTrackingType": 0,
                "BatchNumberScanRequired": "true",
                "SerialNumberScanRequired": "true",
                "StockItemId": "3ae3e4ed-fe9e-4d42-864a-98031e6863d6"
            })

        )
        # print(payload)
        headers = {
            'Accept': 'application/json,text/javascript,*/*;q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Authorization': main_token.token,
        }
        location = requests.post(location_url, data=payload, headers=headers)
        # location = requests.post(location_url, headers=headers)
        print("location_code===>", location.status_code)
        print("location_text===>", location.text)

        return render(request, self.template, locals())
