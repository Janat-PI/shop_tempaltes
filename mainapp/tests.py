from unittest import mock
from django.test import TestCase, RequestFactory
from .models import *
from django.contrib.auth import get_user_model
from decimal import Decimal
from .views import *
from .utils import recalc_cart
User = get_user_model()


class ShopTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Ноутбуки', slug='notebooks')
        self.notebook = Product.objects.create(
            category=self.category,
            title='test',
            slug='test',
            image='asus.png',
            price=Decimal('5000.00')
        )
        self.customer = Customer.objects.create(user=self.user, phone='1111111', address="ADres")
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product = CartProduct.objects.create(
            user=self.customer,
            cart=self.cart,
            content_object=self.notebook
        )

    def test_add_to_cart(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.final_price, Decimal('5000.00'))

    def test_response_from_add_cart_view(self):
        client = RequestFactory()
        request = client.get('')
        request.user = self.user
        response = AddToCartView.as_view()(request, ct_model='notebook', slug='test')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')

    def test_mock_homepage(self):
        mock_data = mock.Mock(status_code=444)
        with mock.patch('mainapp.views.BaseView.get', return_value=mock_data) as mock_data_:
            factory = RequestFactory()
            request = factory.get('')
            request.user = self.user
            response = BaseView.as_view()(request)
            self.assertEqual(response.status_code, 444)




