from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Jobson Lira',
            cpf='12345678901',
            email='jobson.lira@gmail.com',
            phone='27-99882144'
        )
        self.obj.save()

    def test_create(self):
        pass # self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)



