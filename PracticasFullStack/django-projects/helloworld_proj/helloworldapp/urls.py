from django.contrib import admin
from django.urls import path, include
from .views import firstPage, home, contact, blog, createUser, changePassword

urlpatterns = [
    path('firstpage/<int:year>',firstPage,{'example':'firstPage'}),
    path('home',home),
    path('contact',contact),
    path('blog', blog),
    path('createUser/', createUser, name='createUser'),
    path('changePassword/', changePassword, name='changePassword' ),
]