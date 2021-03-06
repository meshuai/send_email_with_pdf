"""send_email_with_pdf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from frontend.views import send_email, upload_pdf, send_email_json

urlpatterns = [
    url(r'^$', send_email, name='send_email'),
    url(r'^send_email_json/$', send_email_json, name='send_email_json'),
    url(r'^upload_pdf/$', upload_pdf, name='upload_pdf'),
]
