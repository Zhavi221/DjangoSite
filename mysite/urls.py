"""
Definition of urls for mysite.
"""

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('news/', include('news.urls')),
    path('streams/', include('streams.urls')),
]
