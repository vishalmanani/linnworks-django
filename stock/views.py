from django.shortcuts import render
from django.views import View


class AuthToken(View):
    template = 'index.html'

    def get(self, request):
        print("call get method")
        return render(request, self.template, locals())
