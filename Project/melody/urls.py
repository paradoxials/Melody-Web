from django.urls import path
from . import views

app_name='melody'
urlpatterns=[
    path('index', views.MelodyIndexView.as_view(), name="index_view"),
    path('registration', views.MelodyRegistrationView.as_view(), name="registration_view"),
]