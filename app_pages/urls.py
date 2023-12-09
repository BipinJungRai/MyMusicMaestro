from django.urls import path
from . import views

# Static Pages
urlpatterns = [
    path('', views.show_home, name='page_home'),
    path('about/', views.show_about, name='page_about'),
    path('contact/', views.show_contact, name='page_contact'),
    path('account/', views.show_account, name='page_account'),
]
