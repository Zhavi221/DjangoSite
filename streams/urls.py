from django.urls import path
from streams import views

app_name = 'streams'
urlpatterns = [
	path('choice/', views.choice, name='choice'),
	path('stream/<str:chosen_stream>/', views.stream, name='stream'),
]