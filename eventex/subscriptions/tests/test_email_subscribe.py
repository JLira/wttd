from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Jobson Lira', cpf='12345678901',
                    email='jobson.lira@gmail.com', phone='27-99911-3254')
        self.client.post('/inscricao/',data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expected = 'Confirmação de inscrição'

        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'jobson.lira@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['jobson.lira@gmail.com','jobson.lira@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Jobson Lira',
            '12345678901',
            'jobson.lira@gmail.com',
            '27-99911-3254',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

