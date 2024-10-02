from django.db import models
from django.contrib.auth.models import AbstractUser



from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=True, default='default_username')

    class Meta:
        db_table = 'myshop_user'
        verbose_name = 'Користувач магазину'
        verbose_name_plural = 'Користувачі магазину'

    # Змінюємо related_name для полів groups та user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myshop_users',
        blank=True,
        verbose_name='Groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myshop_users',
        blank=True,
        verbose_name='User permissions',
        help_text='Specific permissions for this user.',
    )


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateField()
    status = models.CharField(max_length=20)
    items = models.CharField(max_length=20)

    def __str__(self):
        return f'Cart {self.id} - {self.status}'

class Delivery(models.Model):
    country = models.CharField(max_length=30)
    postal_code = models.IntegerField()
    street = models.CharField(max_length=40)
    house_number = models.IntegerField()
    apartment_number = models.IntegerField()

    def __str__(self):
        return f'Delivery {self.id} - {self.country}'

class Status(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.IntegerField()
    payment_type = models.CharField(max_length=10)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order {self.id} - {self.status.name}'

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    price = models.IntegerField()
    brand = models.CharField(max_length=20)
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField()
    model = models.CharField(max_length=20)
    release_date = models.DateField()
    battery_capacity = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    storage_capacity = models.CharField(max_length=20)
    camera_resolution = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return f'Order {self.order.id} - Product {self.product.name}'

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CategoryProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'Category {self.category.name} - Product {self.product.name}'
