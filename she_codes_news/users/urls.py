from django.urls import path
from .views import CreateAccountView, SignUpView


app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # path('user-account/<int:pk>/', AccountView.as_view(), name='userAccount'),
    path('signup/', SignUpView.as_view(), name='signup'),
]