from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product  


class AuthenticationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    
    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, '/products/')
    
    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.', html=True)


class RegistrationTests(TestCase):

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })

        user_exists = User.objects.filter(username='newuser').exists()
        self.assertTrue(user_exists)
        self.assertRedirects(response, '/login/')


class ProductListTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        
        Product.objects.create(name='Test Product 1', price=100, description='Description 1', stock=10)
        Product.objects.create(name='Test Product 2', price=200, description='Description 2', stock=20)
    
    def test_product_list_view(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertContains(response, 'Test Product 1')
        self.assertContains(response, 'Test Product 2')


class LogoutTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, '/login/')
        self.assertFalse('_auth_user_id' in self.client.session)
