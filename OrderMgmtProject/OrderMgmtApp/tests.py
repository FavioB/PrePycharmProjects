from datetime import date

from django.test import TestCase
from .models import Customer, Contact
# Create your tests here.
class ModelTests(TestCase):
    def setUp(self):
        # Create instances for testing
        self.customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            premium_customer=True,
            reliability_rating=5,
            customer_since='2022-01-01',
            cell_phone='123-456-7890',
            home_phone='987-654-3210',
            email='john.doe@example.com',
            created_date='2022-01-01'
        )

        self.address = Address.objects.create(
            customer=self.customer,
            street='123 Main St',
            city='Anytown',
            state='CA',
            zip_code='12345',
            created_date='2022-01-01'
        )

        self.order = Order.objects.create(
            order_number=1,
            customer=self.customer,
            payment_method='Credit Card',
            payment_acct_number='************1234',
            payment_acct_security_code=123,
            order_total=100.00,
            created_date='2022-01-01'
        )

        self.order_details = OrderDetails.objects.create(
            order=self.order,
            product_name='Widget',
            quantity=2,
            created_date='2022-01-01'
        )

    def test_model_creation(self):
        # Testing the creation of each model instance
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderDetails.objects.count(), 1)

    def test_model_update(self):
        # Reading and updating each model instance
        customer = Customer.objects.get(first_name='John')
        address = Address.objects.get(street='123 Main St')
        order = Order.objects.get(order_number=1)
        order_details = OrderDetails.objects.get(product_name='Widget')

        print("Before Update:")
        print(customer)
        print(address)
        print(order)
        print(order_details)

        # Update entities and print
        customer.first_name = 'Updated John'
        customer.save()

        address.street = 'Updated Street'
        address.save()

        order.order_total = 150.00
        order.save()

        order_details.quantity = 3
        order_details.save()

        print("After Update:")
        print(Customer.objects.get(id=customer.id))
        print(Address.objects.get(id=address.id))
        print(Order.objects.get(id=order.id))
        print(OrderDetails.objects.get(id=order_details.id))

    def test_model_read(self):
        # Retrieve entities and print
        print("Customer:")
        print(Customer.objects.get(first_name='John'))

        print("\nAddress:")
        print(Address.objects.get(street='123 Main St'))

        print("\nOrder:")
        print(Order.objects.get(order_number=1))

        print("\nOrder Details:")
        print(OrderDetails.objects.get(product_name='Widget'))