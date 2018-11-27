from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.

# user_list = [
#     {"user": "jack", "pwd": "ggg"},
#     {"user": "jack2", "pwd": "ggg2"},
# ]


def index(request):
    #return HttpResponse("Hello ")
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print('-----------------------------------------')
        print(username, password)
        #temp = {"user": username, "pwd": password}
        models.UserInfo.objects.create(user=username, pwd=password)
        user_list = models.UserInfo.objects.all()
        return render(request, "index2018.html", {"data": user_list})
    return render(request, "index2018.html")

