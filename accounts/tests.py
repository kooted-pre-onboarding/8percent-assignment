import random, bcrypt, jwt

from django.test import TestCase, Client

from accounts.models import User
from eightpercent.settings import SECRET_KEY, ALGORITHM

client = Client()

class SignUpTest(TestCase):
    def setUp(self):
        User.objects.create(id=1, name='hana', email='goodLuck@toyou.com', password='123abc!@')

    def tearDown(self):
        User.objects.all().delete()

    def test_signup_success(self):
        data = {
            'name'     : 'thor', 
            'email'    : 'haveAniceDay@toyou.com', 
            'password' : '123abc!@'
        }
        response = client.post('/accounts/signup', data=data, content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message' : 'SUCCESS'})

    def test_signup_invalid_email(self):
        data = {
            'name'     : 'ruru', 
            'email'    : 'goodLuck@toyou.com', 
            'password' : '123abc!@'
        }
        response = client.post('/accounts/signup', data=data, content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'EXIST_EMAIL'})

    def test_signup_keyerror(self):
        data = {
            'name'    : 'goodLuck@toyou.com',
            'password' : '123abc@'
        }

        response = client.post('/accounts/signin', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})

class SignInTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            name     = 'hana', 
            email    = 'goodLuck@toyou.com', 
            password = bcrypt.hashpw('123abc!@'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )

        global access_token
        access_token = jwt.encode({'user_id' : user.id}, SECRET_KEY, ALGORITHM)

    def tearDown(self):
        User.objects.all().delete()

    def test_signin_success(self):
        data = {
            'email'    : 'goodLuck@toyou.com',
            'password' : '123abc!@'
        }

        response = client.post('/accounts/signin', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'access_token' : access_token})

    def test_signin_invalid_email(self):
        data = {
            'email'    : 'goodLuck111@toyou.com',
            'password' : '123abc@!'
        }

        response = client.post('/accounts/signin', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_USER'})

    def test_signin_invalid_user(self):
        data = {
            'email'    : 'goodLuck@toyou.com',
            'password' : '123abc@'
        }

        response = client.post('/accounts/signin', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_PASSWORD'})

    def test_signin_keyerror(self):
        data = {
            'name'    : 'goodLuck@toyou.com',
            'password' : '123abc@'
        }

        response = client.post('/accounts/signin', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})