from django.contrib import admin
from .models import Departments,About
from .models import Doctors,Booking,Contact
# Register your models here.

admin.site.register(Departments),
admin.site.register(Doctors),
admin.site.register(Booking),
admin.site.register(About),
admin.site.register(Contact),
