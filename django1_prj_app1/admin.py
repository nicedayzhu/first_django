from django.contrib import admin

# Register your models here.
from django1_prj_app1.models import Topic,Entry

admin.site.register(Topic)
admin.site.register(Entry)