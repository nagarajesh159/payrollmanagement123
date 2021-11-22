from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    employeeId = models.CharField(max_length=10, unique=True)
    grade = models.IntegerField()
    date = models.DateTimeField()
    doj = models.DateField()
    dor = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}--{self.employeeId}"


class PaySlip(models.Model):
    month_list = (
        ("jan", "January"),
        ("feb", "February"),
        ("mar", "March"),
        ("apr", "April"),
        ("may", "May"),
        ("june", "June"),
        ("july", "July"),
        ("aug", "August"),
        ("sep", "September"),
        ("oct", "October"),
        ("nov", "November"),
        ("dec", "December"),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    working_days = models.PositiveIntegerField(default=30)
    basic_salary = models.PositiveIntegerField()
    HRA = models.PositiveIntegerField()
    allowance = models.PositiveIntegerField()
    Incentives = models.PositiveIntegerField()
    gift_voucher = models.PositiveIntegerField(null=True, blank=True)
    medical = models.PositiveIntegerField()
    internet = models.PositiveIntegerField(default=1000)
    professional_tax = models.PositiveIntegerField()
    TDS = models.PositiveIntegerField()
    PF = models.PositiveIntegerField()
    month = models.CharField(max_length=15, choices=month_list)

    total_earnings = models.PositiveIntegerField()
    total_deduction = models.PositiveIntegerField()
    net_salary = models.PositiveIntegerField()

    created_at = models.DateField()

    def __str__(self):
        return f"{self.employee.name}-{self.month}-payslip"


