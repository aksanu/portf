from django.contrib import admin
from . import models
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
	list_display= ['title','images','pub_date']

admin.site.register(models.portfolioImages , ImageAdmin)


class subImageAdmin(admin.ModelAdmin):
	list_display= ['img','portfolio']

admin.site.register(models.subImages , subImageAdmin)