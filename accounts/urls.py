from django.urls import path

from . import views

urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('logout',views.logout,name='logout')
]