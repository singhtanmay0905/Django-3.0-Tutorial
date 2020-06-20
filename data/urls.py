from django.urls import path
from data import views

app_name = 'data'

urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),
]
