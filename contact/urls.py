from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    #Contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    #User 
    path('user/register/', views.register, name='register'),
    path('user/login_view/', views.login_view, name='login_view'),
    path('user/logout_view/', views.logout_view, name='logout_view'),
]
