from django.urls import path
from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', start_view),
    path('register_patient',registerp_view,name='register_patient'),
    path('register_doctor',registerd_view,name='register_doctor'),
    path('pregister',pregister_view,name='pregister'),
    path('dregister',dregister_view,name='dregister'),

    
]