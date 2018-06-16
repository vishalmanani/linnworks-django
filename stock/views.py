import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
import requests
from django.views.decorators.csrf import csrf_exempt

from .models import Token


class AuthToken(View):
    template = 'index.html'

    def get(self, request):
        token = request.GET.get('token', None)
        print("token=======>", token)

        url = 'https://api.linnworks.net//api/Auth/AuthorizeByApplication'
        # payload = {
        #     "applicationId": "65625950-d006-4e8f-a5a4-b3c8e1ca4cfe",
        #     "applicationSecret": "8f0df2ed-9338-402b-9dd8-4b3efa560d0e",
        #     "token": token,
        # }
        # payload = {
        #     "applicationId": "214ae235-33f1-439b-b5cc-ce18fd22fbee",
        #     "applicationSecret": "8dedcb4c-e4bb-4a24-ac18-5b8fc515814c",
        #     "token": token,
        # }

        payload = {
            "applicationId": "10b0147f-c451-423a-9df8-b5c2c3841ad7",
            "applicationSecret": "a01e7d34-7483-4b3f-9709-b85f824edcbd",
            "token": token,
        }

        response = requests.post(url, data=payload)

        print("AuthorizeByApplication status_code====>", response.status_code)
        print("AuthorizeByApplication status_text====>", response.text)

        my_token = json.loads(response.text)
        main_token = my_token.get('Token')
        print(main_token)
        Token.objects.create(token=main_token)

        return render(request, self.template, locals())


class TestApi(View):
    template = 'index.html'

    def get(self, request):
        main_token = Token.objects.last()
        print("main_token last===>", main_token.token)
        # location_url = "https://eu-ext.linnworks.net//api/Inventory/UpdateInventoryItem"
        # location_url = "https://eu-ext.linnworks.net//api/Stock/SetStockLevel"
        # location_url="https://eu-ext.linnworks.net//api/Inventory/GetCategories"
        # location_url="https://eu-ext.linnworks.net//api/Inventory/GetPackageGroups"
        # location_url = "https://eu-ext.linnworks.net//api/ProcessedOrders/SearchProcessedOrdersPaged"
        location_url = "https://eu-ext.linnworks.net//api/Orders/GetOrderItems"
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

        # payload = dict(
        #     from='2018-02-19',
        #     to='2018-02-19',
        #     dateType='0',
        #     searchField='sample string 1',
        #     exactMatch='true',
        #     searchTerm='sample string 1',
        #     pageNum='1',
        #     numEntriesPerPage = '100',
        # )

        # payload = dict(
        #     dateType='0',
        #     searchField='nOrderId',
        #     exactMatch="true",
        #     searchTerm="100003",
        #     pageNum="1",
        #     numEntriesPerPage="10"
        # )

        payload = dict(
            orderId='f635e1c6-fc7c-48d9-af7b-5bba4b859186',
            fulfilmentCenter='00000000-0000-0000-0000-000000000000'
        )

        # payload = dict(
        #
        #     inventoryItem=json.dumps({
        #         # "VariationGroupName": "sample string 1",
        #         "Quantity": 500,
        #         "InOrder": 200,
        #         "Due": 300,
        #         "MinimumLevel": 10,
        #         "Available": 10,
        #         "CreationDate": "2018-02-19T16:57:06.8269989+00:00",
        #         "IsCompositeParent": "true",
        #         "ItemNumber": "A1001",
        #         "ItemTitle": "sample string 6",
        #         "BarcodeNumber": "sample string 7",
        #         "MetaData": "sample string 8",
        #         "isBatchedStockType": "false",
        #         "PurchasePrice": 20,
        #         "RetailPrice": 20,
        #         "TaxRate": 10,
        #         "PostalServiceId": "00000000-0000-0000-0000-000000000000",
        #         "PostalServiceName": "Default",
        #         "CategoryId": "00000000-0000-0000-0000-000000000000",
        #         "CategoryName": "Default",
        #         "PackageGroupId": "00000000-0000-0000-0000-000000000000",
        #         "PackageGroupName": "Default",
        #         "Height": 17.1,
        #         "Width": 18.1,
        #         "Depth": 19.1,
        #         "Weight": 20.1,
        #         "InventoryTrackingType": 0,
        #         "BatchNumberScanRequired": "true",
        #         "SerialNumberScanRequired": "true",
        #         "StockItemId": "3ae3e4ed-fe9e-4d42-864a-98031e6863d6"
        #     })
        #
        # )
        # print(payload)
        headers = {
            'Accept': 'application/json,text/javascript,*/*;q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Authorization': 'd4a57695-4e5f-48e4-b5e0-198ade12ec0b',
        }
        location = requests.post(location_url, data=payload, headers=headers)
        # location = requests.post(location_url, headers=headers)
        print("location_code===>", location.status_code)
        print("location_text===>", location.text)

        return render(request, self.template, locals())
