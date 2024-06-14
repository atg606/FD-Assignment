from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'email', 'address')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('customer_id',)
