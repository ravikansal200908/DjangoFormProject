from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_delete = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='cat_img/', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    is_delete = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='pro_img/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    PENDING = 'Pending'
    PROCESSED = 'Processed'
    CANCELED = 'Canceled'

    ORDER_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSED, 'Processed'),
        (CANCELED, 'Canceled'),
    ]

    customer_name = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product)
    order_status = models.CharField(max_length=20, choices=ORDER_CHOICES)

    def __str__(self):
        return f"{self.customer_name} Order {self.get_order_status_display()}"
