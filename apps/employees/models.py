from django.db import models
from apps.core.models import AbstractBaseModel

# Create your models here.
STATUS_CHOICES = (
    ("Absent", "Absent"),
    ("Present", "Present"),
)

LEAVE_TYPES = (
    ("Sick Leave", "Sick Leave"),
    ("Emergency Leave", "Emergency Leave"),
    ("Normal Leave", "Normal Leave"),
)

LEAVE_STATUS_CHOICES = (
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
    ("Pending Review", "Pending Review"),
)


class EmployeeDocument(AbstractBaseModel):
    employee = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="employeedocuments")
    police_clearance = models.FileField(upload_to="police_clearances/", null=True, blank=True)
    chief_letter = models.FileField(upload_to="chief_letters/", null=True, blank=True)
    referee_letter = models.FileField(upload_to="recommended_letters/", null=True, blank=True)
    scanned_id = models.FileField(upload_to="scanned_ids/", null=True, blank=True)
    kcse_certificate = models.FileField(upload_to="kcse_certificates/", null=True)
    kcpe_certificate = models.FileField(upload_to="kcpe_certificates/", null=True)
    college_certificate = models.FileField(upload_to="college_certificates/", null=True)
    kra_certificate = models.FileField(upload_to="kra_certificates", null=True)

    def __str__(self):
        return self.employee.username
    


class Attendance(AbstractBaseModel):
    employee = models.ForeignKey("users.User", on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    checkin_time = models.DateTimeField(null=True)
    checkout_time = models.DateTimeField(null=True, blank=True)
    checked_in_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="checkinmanagers",
    )
    marked = models.BooleanField(default=False)
    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, null=True, blank=True
    )

    def __str__(self):
        return self.employee.first_name + " " + self.employee.last_name


class EmployeeLeave(AbstractBaseModel):
    employee = models.ForeignKey("users.User", on_delete=models.CASCADE)
    days_applied = models.IntegerField(default=1)
    leave_type = models.CharField(max_length=255, choices=LEAVE_TYPES)
    status = models.CharField(
        max_length=255, choices=LEAVE_STATUS_CHOICES, default="Pending Review"
    )
    leave_from = models.DateField(null=True, blank=True)
    leave_to = models.DateField(null=True)
    approved_by = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="leaveapprovers",
    )

class EducationInformation(AbstractBaseModel):
    employee = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="educationdetails")
    level = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    start_year = models.CharField(max_length=255, null=True)
    graduation_year = models.CharField(max_length=255)

    def __str__(self):
        return self.school_name

class BankInformation(AbstractBaseModel):
    employee = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="bankingdetails")
    bank_name  = models.CharField(max_length=255, default="Equity Bank Kenya")
    branch_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255, null=True)
    account_number = models.CharField(max_length=255)

    def __str__(self):
        return self.account_name
    

class NextOfKin(AbstractBaseModel):
    employee = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="nextofkins")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    relation = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name