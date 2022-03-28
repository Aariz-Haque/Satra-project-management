from django.contrib import admin
from .models import Beneficiary,Patient,Report,Camp,ScreeningCamp
# Register your models here.
admin.site.register(Beneficiary)
admin.site.register(Patient)
admin.site.register(Report)
admin.site.register(Camp)

@admin.register(ScreeningCamp)
class ScreeningCampAdmin(admin.ModelAdmin):
    search_fields = ['name','id','date_of_camp']
    class Media:
        js = ('tiny.js',)