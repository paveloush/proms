from django.contrib import admin
from .models import *


# Register your models here.


# class TagInline(admin.TabularInline):
#     model = Tag
#
#
# class RegionInline(admin.TabularInline):
#     model = Region
#
#
# class PromiseAdmin(admin.ModelAdmin):
#     inlines = [TagInline, RegionInline, ]


admin.site.register( Promise,)

admin.site.register(Status)
admin.site.register(Region)  # REGION!!
admin.site.register(Tag)
