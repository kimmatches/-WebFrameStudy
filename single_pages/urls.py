
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.landing), #아무것도 없을 떄 대문 페이지 보여주기
    path('about_me/', views.about_me),
]
