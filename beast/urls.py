from django.urls import path
from . import views  # Ensure you're importing the views module
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Route for the home view
    path('cookie-policy/', views.cookie_policy, name='cookie-policy'),  # Route for the cookie policy view
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),  # Route for the privacy policy view
    path('data-protection-policy/', views.data_protection_policy, name='data-protection-policy'),  # Route for the data protection policy view
    path('participant-privacy-notice/', views.participant_privacy_notice, name='participant-privacy-notice'),  # Route for the participant privacy notice view
    path('404/', views.error_404, name='error-404'),  # Route for the 404 view
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)