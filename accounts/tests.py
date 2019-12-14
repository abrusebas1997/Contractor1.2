from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from accounts.forms import UserCreationForm
​

class RegisterViewTest(TestCase):

     # Tests to see that there is a sign up page
    def test_one_page(self):
        response = self.client.get(reverse_lazy('templates-signup-page'))
        self.assertEqual(response.status_code, 200)
​
​
class FormCreationTest(TestCase):
    """ To test form creation """
    # To test a sign in form is valid
    def test_form(self):
​
        form_info = {
            'username': 'chao1',
            'email': 'test@testing.com',
            'password1': 'password',
            'password2': 'password',
         }
​
        form = UserCreationForm(data=form_info)
        self.assertTrue(form.is_valid())
