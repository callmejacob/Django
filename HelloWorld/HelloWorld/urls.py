"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from . import view, testdb, search, search2

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb/add$', testdb.add),
    url(r'^testdb/query$', testdb.query),
    url(r'^testdb/update$', testdb.update),
	url(r'^testdb/delete$', testdb.delete),
	url(r'^search-form$', search.search_from),
	url(r'^search$', search.search),
	url(r'^search-post$', search2.search_post),
	url(r'^admin/', admin.site.urls),
	url(r'^travel$', view.travel),
	url(r'^travel-post$', view.travel_post),
]

