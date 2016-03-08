"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include('admin.site.urls'),
    url(r'^login/', include('qa.views.test'),
    url(r'^signup/', include('qa.views.test'),
    url(r'^question/\w+/', include('qa.views.test'),
    url(r'^ask/', include('qa.views.test'),
    url(r'^popular/', include('qa.views.test'),
    url(r'^new/', include('qa.views.test'),
]
