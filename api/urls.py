from django.urls import path

from api import views

urlpatterns = [
    path('', views.login_handler),
    path('logout_me/', views.logout_handler)
]
