from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetail.as_view(), name='news_detail'),
]