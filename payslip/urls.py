from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.add_new_employee, name="new"),
    path('<str:emp_id>/payroll/', views.add_payslip, name="new_payroll"),
]
