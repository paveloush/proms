from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Promise)
admin.site.register(Person)
admin.site.register(Status)
admin.site.register(Region)  # REGION!!
admin.site.register(Tag)
admin.site.register(Ip)