from django.urls import path
from . import views

app_name='melody'
urlpatterns=[
    path('index', views.MelodyIndexView.as_view(), name="index_view"),
    path('customerRegistration', views.MelodyCustomerRegistrationView.as_view(), name="customerRegistration_view"),
    path('dashboard', views.MelodyDashboardView.as_view(), name="dashboard_view"),
    path('songRegistration', views.MelodySongRegistrationView.as_view(), name="songRegistration_view"),
]