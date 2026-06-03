from django.contrib import admin
from .models import Order, OrderedItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderedItem
    extra = 0
    readonly_fields = ['product','quantity','price','total_price']

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedItem)