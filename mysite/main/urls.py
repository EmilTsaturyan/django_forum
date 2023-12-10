from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('forum/', views.forum, name='forum'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),  
]

