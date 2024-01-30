from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


def thanks(request):
    return HttpResponse("This is thanks page. app3")
