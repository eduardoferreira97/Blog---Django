from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail',views.detail, name='detail'),
    path('post/new',views.post, name='new_post'),
    path('<int:pk>/edit',views.edit, name='edit')
]