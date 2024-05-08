from django.urls import path
from user.apis import auth as user_auth_apis

urlpatterns = [
   path('login',user_auth_apis.LoginAPI.as_view())
]