from django.db import models

# Customer entity
class Customer(models.Model):
    # Attributes for the Customer entity
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    premium_customer = models.BooleanField()
    reliability_rating = models.IntegerField()
    customer_since = models.DateField()
    cell_phone = models.CharField(max_length=15)
    home_phone = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    created_date = models.DateField()

    # __str__ method to represent the instance as a string
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# the meta class is used to specify the default ordering for a models queryset.
# It defines the default way instances of the model are ordered in queries unless otherwise specified
    class Meta:
        ordering = ['first_name']

# Address entity
class Address(models.Model):
    # Foreign key to the Customer entity
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Attributes for the Address entity
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=11)
    created_date = models.DateField()

    # __str__ method for string representation
    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"

    class Meta:
        ordering = ['street']

# Order entity
class Order(models.Model):
    # Foreign key to the Customer entity
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Attributes for the Order entity
    order_number = models.IntegerField()
    payment_method = models.CharField(max_length=10)
    payment_acct_number = models.CharField(max_length=20)
    payment_acct_security_code = models.IntegerField()
    order_total = models.FloatField()
    created_date = models.DateField()

    def __str__(self):
        return f"Order ID: {self.order_number}, Date: {self.created_date}"

    class Meta:
        ordering = ['customer']

# Order_Details entity
class OrderDetails(models.Model):
    # Foreign key to the Order entity
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # Attributes for the Order_Details entity
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    created_date = models.DateField()

    def __str__(self):
        return f"Product: {self.product_name}, Quantity: {self.quantity}"

    class Meta:
        ordering = ['order']
# Create your models here.
