from django.db import models
from django.contrib.auth.models import User

# This model represents the different types of items (e.g., Vegetables, Fruits)
class Type(models.Model):
    name = models.CharField(max_length=200)  # Name of the type (e.g., Vegetables, Fruits)

    def __str__(self):
        return self.name  # Return the name of the type as a string representation

# This model represents the items available in the store, which belong to a certain type (e.g., Carrot in Vegetables)
class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)  # Each item is linked to a Type
    name = models.CharField(max_length=200)  # Name of the item (e.g., Carrot)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the item, allowing for two decimal places
    stock = models.PositiveIntegerField(default=100)  # Number of items in stock, defaults to 100
    available = models.BooleanField(default=True)  # Boolean to check whether the item is available for sale
    description = models.TextField(null=True, blank=True)  # Optional field for item description

    def __str__(self):
        return self.name  # Return the name of the item as a string representation

# This model extends Django's built-in User model to include additional fields for clients
class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'Waterloo'),
    ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)  # Client's shipping address (optional)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')  # Client's city with a default of Chatham
    interested_in = models.ManyToManyField(Type)  # Many-to-Many relationship showing which types the client is interested in
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Optional phone number field for the client

    def __str__(self):
        return self.username  # Use the username of the client as a string representation

# This model tracks the items that clients have ordered and their order status
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Link each order item to an Item
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Link each order item to a Client
    quantity = models.PositiveIntegerField(default=1)  # Number of units of the item ordered, defaults to 1
    STATUS_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Placed'),
        (2, 'Shipped'),
        (3, 'Delivered'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)  # Status of the order (e.g., placed, shipped, delivered)
    last_updated = models.DateTimeField(auto_now=True)  # Automatically record when the order was last updated

    # Calculate the total price for the given quantity of items in the order
    def total_price(self):
        return self.item.price * self.quantity

    def __str__(self):
        # String representation of the order showing the client's username and item name
        return f"{self.client.username} - {self.item.name}"
