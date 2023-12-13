from django.urls import path

from . import views
from .views import login_view

# Static Pages
urlpatterns = [
    path('', views.show_home, name='page_home'),
    path('about/', views.show_about, name='page_about'),
    path('contact/', views.show_contact, name='page_contact'),
    path('login/', login_view, name='page_login'),
    path('recommend-a-friend/', views.recommend_friend, name='recommend_friend'),
]
