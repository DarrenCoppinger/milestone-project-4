from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'full_name', 'date', 'time')
    readonly_fields = ('date', 'time')
    inlines = (OrderLineAdminInLine, )


admin.site.register(Order, OrderAdmin)
