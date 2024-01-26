from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse

def register2(reguest):
    return HttpResponse("this is the third registeration page")



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("crm.urls")),
    path("register2", register2),
]
