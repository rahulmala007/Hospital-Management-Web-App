"""hosmanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from logins.views import login, logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/',include(('profiles.urls','profiles'),namespace='profiles')),
    path('login/', login,name='login'),
    path('logout/', logout),
    path('home/',include(('home.urls','home'),namespace='home')),
    path('logins/',include('logins.urls')),
    path('bills/',include('bills.urls')),
    path('appointments/',include(('appointments.urls','appointments'),namespace='appointments')),
    path('cases/',include(('all_cases.urls','case'),namespace='case')),
    path('',include(('register.urls','register'),namespace='register'))
]
