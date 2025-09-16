from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('ngo/<int:ngo_id>/', views.ngo_approval, name='ngo_approval'),
    path('reports/', views.reports_view, name='reports'),
]
