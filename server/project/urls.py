from django.urls import path
from . import views

urlpatterns=[
    path('', views.Index , name='Index'),
    path('mechanic/',views.MechanicView, name='mechanic'),
    path('car-info/',views.CarInformation, name='car-info'),
    path('service-list/',views.CarService, name='service-list'),
    path('autoshops-list/',views.AutoshopList, name='autoshops-list'),
    path('company/',views.CompanyProfile, name='company'),
    path('tow-service/',views.TowService, name='tow-service'),
    path('tow-service-results/',views.TowServiceResults, name='tow-service-results'),
    path('profile/',views.ProfilePage, name='profile'),
    path('my-services/',views.MyServices, name='my-services'),

    # Admins Urls 
    path('dashboard/',views.Dashboard, name='dashboard'),
    path('edit-company/',views.CompanyEdit, name='edit-company'),
]