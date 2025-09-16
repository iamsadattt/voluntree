from django.urls import path
from . import views

urlpatterns = [
    path('', views.ngo_dashboard, name='ngo_dashboard'),
    path('create/', views.create_event, name='create_event'),
    path('manage/', views.manage_events, name='manage_events'),
    path('applications/<int:event_id>/', views.view_applications, name='view_applications'),
]
