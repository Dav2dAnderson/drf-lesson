from django.urls import path

from .views import UserLoginAPIView, UserRegisterAPIView, UserLogOutAPIView, UserProfileAPIView, UserCommentsAPIView


urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
    path('register/', UserRegisterAPIView.as_view()),
    path('logout/', UserLogOutAPIView.as_view()),
    path('my-profile/', UserProfileAPIView.as_view()),
    path('my-comments/', UserCommentsAPIView.as_view())
]





