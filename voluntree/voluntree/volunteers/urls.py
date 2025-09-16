from django.urls import path
from . import views

urlpatterns = [
    path('', views.volunteer_dashboard, name='volunteer_dashboard'),
    path('browse/', views.browse_events, name='browse_events'),
    path('event/<int:event_id>/', views.event_details, name='event_details'),
    path('profile/', views.profile_view, name='volunteer_profile'),
    path('certificates/', views.certificates_view, name='my_certificates'),
]
