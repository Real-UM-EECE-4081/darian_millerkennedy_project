from django.test import TestCase
from django.contrib.auth import get_user_model, get_user
from django.urls import reverse
from signup_app.models import Contacts

# Create your tests here.
class Tests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'johnnydd019'
    
    def test_signup_page_url(self):
        response = self.client.get("/signup")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='signup.html')
    
    def test_homepage_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='homepage.html')
    
    def test_add_contact_url(self):
        response = self.client.post("/contactadd")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='contactadd.html')
    
    def test_signup_form(self):
            response = self.client.post(reverse('signup'), data={
                'username': self.username,
                'email': self.email,
                'password1': self.password,
                'password2': self.password
            })
            
            self.assertEqual(response.status_code, 302)

            users = get_user_model().objects.all()
            self.assertEqual(users.count(), 1)
    
     
    def test_login(self):
        response = self.client.get('/signin')
        self.assertEquals(response.status_code, 200)
        self.client.login(username= self.username, password=self.email)
        self.assertTrue('Log in' in response.content)

    def test_logout(self):
        self.client.login(username= self.username, password=self.email)
        response = self.client.get('/signin')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log out' in response.content)
        self.client.logout()
        

class TestModels(TestCase):
    def addproduct(self):
        contact =  Contacts.objects.create(name='John', number='901335678', description='My brother')
        contact.save()
        contacttest = Contacts.objects.get(name='John')
        self.assertEqual(contact, contacttest)
    
    def updateprice(self):
        contact =  Contacts.objects.create(name='John', number='901335678', description='My brother')
        contact.save()
        contact.number = '88678737484'
        contact.save()
        contacttest = Contacts.objects.get(name='John')
        self.assertEqual(contact, contacttest)
    