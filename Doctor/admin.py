from django.contrib import admin

# Register your models here.
from Doctor.models import Session, Doctor, Specialty

admin.site.register(Doctor)
admin.site.register(Specialty)
admin.site.register(Session)
