from django.urls import path
from .views import CreateAccountView, AccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('user-account/', AccountView.as_view(), name='userAccount'),
]