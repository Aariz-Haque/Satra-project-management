from django.contrib import admin
from .models import Beneficiary,Patient,Report
# Register your models here.
admin.site.register(Beneficiary)
admin.site.register(Patient)
admin.site.register(Report)