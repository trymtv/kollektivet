from django.contrib import admin
from .models import Wash, WashQueue

# Register your models here.
admin.site.register(Wash)
admin.site.register(WashQueue)