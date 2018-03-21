from django.shortcuts import render
from django.views import View


class AuthToken(View):
    template = 'index.html'

    def get(self, request):
        print("call get method")
        token = request.GET.get('token', None)
        print("token=======>", token)
        return render(request, self.template, locals())
