from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee, PaySlip
from datetime import timezone

# Create your views here.


def index(request):
    emp_list = Employee.objects.all()
    return render(request, "index.html", {"emp_list": emp_list})


def add_new_employee(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST['name'],
            employeeId=request.POST['employeeId'],
            dor=request.POST['date']

        )
        return HttpResponseRedirect(reverse("index"))
    return render(request, "new_employee.html")


def add_payslip(request, emp_id):
    employee = get_object_or_404(Employee, employeeId=emp_id)
    if request.method == "POST":
        employee.paySlip_set.create(
            # employee=request.POST['employee'],
            working_days=request.POST['working_days'],
            basic_salary=request.POST['basic_salary'],
            HRA=request.POST['HRA'],
            allowance=request.POST['allowance'],
            Incentives=request.POST['Incentives'],
            gift_voucher=request.POST['gift_voucher'],
            medical=request.POST['medical'],
            internet=request.POST['internet'],
            professional_tax=request.POST['professional_tax'],
            TDS=request.POST['TDS'],
            PF=request.POST['PF'],
            month=request.POST['month'],

            total_earnings=request.POST['total_earnings'],
            total_deduction=request.POST['total_deduction'],
            net_salary=request.POST['net_salary'],
        )
        return HttpResponseRedirect(reverse("index"))
    return render(request, "new_payslip.html")


def get_pay_slip(request, emp_id):
    employee = get_object_or_404(Employee, employeeId=emp_id)
    employee.paySlip_set.orderby('-created_at')
    return HttpResponse("payslip")


