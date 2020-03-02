from django.urls import path
from discordTool.views import members_list

app_name = 'discordTool'
urlpatterns = [
	path('', members_list, name="home"),
]
