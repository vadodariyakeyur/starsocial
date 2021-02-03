from django.contrib import admin
from . import models

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

# Register your models here.
admin.site.register(models.Group)
