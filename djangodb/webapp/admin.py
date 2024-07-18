from django.contrib import admin
from .models import Member, Location, Risk, Audit

# Register your models here.
admin.site.register(Member),
admin.site.register(Location),
admin.site.register(Risk),
admin.site.register(Audit),
