from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail',views.detail, name='detail'),
    path('<int:pk>/post_detail',views.post, name='post'),
]