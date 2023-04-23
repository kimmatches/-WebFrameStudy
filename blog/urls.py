
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostList.as_view()), # CBV 방식의 함수 호출 # 클래스 방식
    # path('', views.index), # FBV 방식의 함수 호출
    path('<int:pk>/', views.PostDetail.as_view()), # CBV, 키를 이용해서 하나만 검색해온다.
    # path('<int:pk>/', views.single_post_page), # FBV 상세페이지
]
