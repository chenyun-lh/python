from django.conf.urls import url
from django.contrib import admin
from book.views import index

urlpatterns = [
    url(r'^index/$', index)
    ]