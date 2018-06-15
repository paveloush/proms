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


class PromiseAdmin(admin.ModelAdmin):
    list_display = ['person', 'title', 'finish_date', 'status', 'vote_up', 'vote_down',]
    list_filter = ['finish_date', 'status', 'tag']
    search_fields = ['text']


    class Meta():
        model = Promise

admin.site.register(Promise, PromiseAdmin)

admin.site.register(Status)
admin.site.register(Region)  # REGION!!
admin.site.register(Tag)
