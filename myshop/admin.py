from django.contrib import admin
from .models import User, ShoppingCart, Delivery, Status, Order, Product, OrderProduct, Category, CategoryProduct

# Реєстрація моделей для Django Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number')
    list_display_links = ('id', 'first_name', 'last_name')  # Посилання на редагування моделі
    search_fields = ('first_name', 'last_name', 'email')   # Поле для пошуку

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_creation', 'status')
    list_filter = ('status', 'date_creation')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')  # Пошук за допомогою зв'язаного поля

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'postal_code', 'street', 'house_number', 'apartment_number')
    list_filter = ('country',)
    search_fields = ('country', 'postal_code', 'street')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery', 'date', 'price', 'payment_type', 'status')
    list_filter = ('status', 'date')
    search_fields = ('user__first_name', 'user__last_name', 'delivery__country')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'brand', 'image', 'quantity', 'model', 'release_date',
                    'battery_capacity', 'memory', 'storage_capacity', 'camera_resolution')
    list_filter = ('brand', 'price', 'release_date')
    search_fields = ('name', 'brand', 'description')

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'brand', 'image', 'quantity')
        }),
        ('Details', {
            'fields': ('model', 'release_date', 'battery_capacity', 'memory', 'storage_capacity', 'camera_resolution')
        }),
    )

    readonly_fields = ('id',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('name',)
        return self.readonly_fields

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'price', 'count')
    list_filter = ('order__user__first_name', 'product__brand')
    search_fields = ('order__user__first_name', 'product__name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'product')
    list_filter = ('category__name',)
    search_fields = ('product__name', 'category__name')
