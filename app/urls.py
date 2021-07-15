from django.urls import path, include

from app.views import AnnounceGenericAPIView, CommentGenericAPIView, LogementGenericAPIView

urlpatterns = [
    path('announces', AnnounceGenericAPIView.as_view()),
    path('announces/<str:pk>', AnnounceGenericAPIView.as_view()),
    path('announces/<str:pk>', AnnounceGenericAPIView.as_view()),

    path('announces/<str:pk>/comments', CommentGenericAPIView.as_view()),

    path('announces/<str:pk>/logements', LogementGenericAPIView.as_view()),

]
