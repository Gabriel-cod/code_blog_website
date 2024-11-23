from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/login/', views.SignInView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]