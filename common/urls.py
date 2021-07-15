from django.urls import path, include

# from .views import RegisterAPIView, LoginAPIView, UserAPIView, LogoutAPIView
#
# urlpatterns = [
#     path('register', RegisterAPIView.as_view()),
#     path('login', LoginAPIView.as_view()),
#     path('logout', LogoutAPIView.as_view()),
#     path('user', UserAPIView.as_view())
# ]
from common.api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]
