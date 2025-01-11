"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from beast import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('data-protection-policy/', views.data_protection_policy, name='data_protection_policy'),
    path('participant-privacy-notice/', views.participant_privacy_notice, name='participant_privacy_notice'),
]

handler404 = 'beast.views.error_404'
