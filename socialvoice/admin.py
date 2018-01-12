from django.contrib import admin
from .models import Lead


class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'message')


admin.site.register(Lead, LeadAdmin)

