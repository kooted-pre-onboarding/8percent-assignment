import json, jwt, bcrypt
from datetime              import date, datetime, timedelta

from django.test           import TestCase, Client

from eightpercent.settings import SECRET_KEY, ALGORITHM
from accounts.models       import User, Account
from transactions.models   import Transaction, TransactionType


class DepositTransactionView(TestCase):
    def setUp(self):
        password = 'sample_password'
        user = User.objects.create(
            id       = 1,
            email    = "example@naver.com",
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            name     = '김참작'
        )

        self.token = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

        Account.objects.create(
            id      = 1,
            number  = "5487-6848-6848-6847",
            balance = 300000,
            user_id = 1,
        )

        TransactionType.objects.create( id = 1, name = "입금" )

    def tearDown(self):
        User.objects.all().delete()
        Account.objects.all().delete()
        TransactionType.objects.all().delete()

    def test_deposit_transaction_post_success(self):
        client = Client()

        headers = {'HTTP_Authorization': self.token}
        data = {"amount" : 10000, "sum_up" : "5"}

        response = client.post(
            "/transactions/deposit",
            json.dumps(data),
            content_type="application/json",**headers
        )
        self.assertEqual(response.status_code, 201)

    def test_deposit_transaction_post_invalid_input(self):
        client = Client()

        headers = {'HTTP_Authorization': self.token}
        data = {"amount" : -10000, "sum_up" : "5"}

        response = client.post(
            "/transactions/deposit",
            json.dumps(data),
            content_type="application/json",**headers
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_INPUT"})

    def test_deposit_transaction_post_type_error(self):
        client = Client()

        headers = {'HTTP_Authorization': self.token}
        data = {"amount" : "10000", "sum_up" : 5}

        response = client.post(
            "/transactions/deposit",
            json.dumps(data),
            content_type="application/json",**headers
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "TYPE_ERROR"})

    def test_deposit_transaction_post_key_error(self):
        client = Client()

        headers = {'HTTP_Authorization': self.token}
        data = {"amount" : 10000}
        
        response = client.post(
            "/transactions/deposit",
            json.dumps(data),
            content_type="application/json", **headers
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})


class WithdrawTransactionTest(TestCase):
    def setUp(self):
        password = 'sample_password'
        user = User.objects.create(
            id       = 1,
            email    = "example@naver.com",
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            name     = '김참작'
        )

        self.token = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

        Account.objects.create(
            id      = 1,
            number  = "5487-6848-6848-6847",
            balance = 30000,
            user_id = 1,
        )

        TransactionType.objects.create(id=2, name="출금")

    def tearDown(self):
        User.objects.all().delete()
        Account.objects.all().delete()
        TransactionType.objects.all().delete()

    def test_withdrawal_post_success(self):
        client = Client()

        headers = {'HTTP_Authorization': self.token}
        data = {"amount" : 10000, "sum_up" : 5}

        response = client.post(
            "/transactions/withdraw",
            json.dumps(data),
            content_type="application/json",
            **headers
        )
        self.assertEqual(response.status_code, 201)

    def test_withdrawal_post_invalid_input(self):
        client = Client()

        headers = {'HTTP_Authorization': self.token}
        data = {"amount" : -10000, "sum_up" : 5}

        response = client.post(
            "/transactions/withdraw",
            json.dumps(data),
            content_type="application/json",
            **headers
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "INVALID_INPUT"})

    def test_withdrawal_post_exceed_input(self):
        client = Client()

        headers = {'HTTP_Authorization': self.token}
        data = {"amount" : 50000, "sum_up" : 5}

        response = client.post(
            "/transactions/withdraw",
            json.dumps(data),
            content_type="application/json",
            **headers
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "WRONG_REQUEST"})

    def test_withdrawal_post_type_error(self):
        client = Client()

        headers = {'HTTP_Authorization': self.token}
        data = {"amount" : "10000", "sum_up" : 5}

        response = client.post(
            "/transactions/withdraw",
            json.dumps(data),
            content_type="application/json",
            **headers
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "TYPE_ERROR"})

    def test_withdrawal_post_key_error(self):
        client = Client()

        headers = {'HTTP_Authorization': self.token}
        data = {"amount" : 10000}

        response = client.post(
            "/transactions/withdraw",
            json.dumps(data),
            content_type="application/json",
            **headers
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "KEY_ERROR"})


class TransactionListTest(TestCase):
    def setUp(self):
        password = 'testpassword2@'
        user = User.objects.create(
            id       = 1,
            name     = 'test_user',
            email    = 'test@gmail.com',
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        self.access_token = jwt.encode({'user_id':user.id}, SECRET_KEY, algorithm=ALGORITHM)

        Account.objects.create(
            id      = 1,
            number  = '1111-1111-1111-1111',
            balance = 0,
            user_id = 1
        )
        
        TransactionType.objects.bulk_create([
            TransactionType(id = 1, name = 'deposit'),
            TransactionType(id = 2, name = 'withdraw')
        ])
        
        Transaction.objects.bulk_create([
            Transaction(id                  = 1,
                        transaction_type_id = 1,
                        amount              = 10000,
                        sum_up              = '만원 입금',
                        account_id          = 1,
                        balance_after_transaction = 10000,
            ),
            Transaction(id                  = 2,
                        transaction_type_id = 2,
                        amount              = 10000,
                        sum_up              = '만원 출금',
                        account_id          = 1,
                        balance_after_transaction = 0,
            )
        ])

    def tearDown(self):
        User.objects.all().delete()
        Account.objects.all().delete()
        TransactionType.objects.all().delete()
        Transaction.objects.all().delete()
    
    def test_transaction_list_get_success(self):
        created_at1 = Transaction.objects.get(id=1).created_at
        created_at2 = Transaction.objects.get(id=2).created_at
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?start-date={date.today()}&end-date={date.today()}&order=created_at',
                              **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                        {'data': [
                            {
                                "datetime": datetime.strftime(created_at1, '%Y-%m-%d %H:%M:%S'),
                                "amount": 10000,
                                "balance": 10000,
                                "type": "deposit",
                                "sum_up": "만원 입금"
                            },
                            {
                                "datetime": datetime.strftime(created_at2, '%Y-%m-%d %H:%M:%S'),
                                "amount": 10000,
                                "balance": 0,
                                "type": "withdraw",
                                "sum_up": "만원 출금"
                            }
                        ]
                    })
        
    def test_transaction_list_empty_order_fail(self):
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?start-date={date.today()}&end-date={date.today()}',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'ORDER_CAN_NOT_BE_EMPTY'})

    def test_transaction_list_empty_date_range_fail(self):
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?order=created_at',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'DATE_RANGE_CAN_NOT_BE_EMPTY'})

    def test_transaction_list_invalid_date_range_fail(self):
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?start-date={date.today()}&end-date={date.today()-timedelta(days=1)}&order=created_at',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'INVALID_DATE_RANGE'})

    def test_transaction_list_value_error_fail(self):
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?start-date={date.today()}&end-date=wrong!!!!&order=create_at',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'VALUE_ERROR'})

    def test_transaction_list_field_error_fail(self):

        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?start-date={date.today()}&end-date={date.today()}&order=wrong!!!!',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'FIELD_ERROR'})