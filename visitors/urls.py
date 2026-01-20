from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_visitor, name='register_visitor'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/export/csv/', views.dashboard_export_csv, name='dashboard_export_csv'),
    path('dashboard/export/excel/', views.dashboard_export_excel, name='dashboard_export_excel'),
    path('dashboard/delete/<int:visitor_id>/', views.delete_visitor, name='delete_visitor'),
]
