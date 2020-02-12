from datetime import datetime
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app import forms
from accounts import views
from django.conf import settings

app_name = 'accounts'
urlpatterns = [
    path('login/',
         LoginView.as_view
         (
             template_name='accounts/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page=(settings.LOGOUT_REDIRECT_URL)), name='logout'),
    path('signup/', views.signup, name='signup'),
    ]


