import jwt, bcrypt
from datetime              import date, datetime, timedelta

from django.test           import TestCase, Client

from eightpercent.settings import SECRET_KEY, ALGORITHM
from accounts.models       import User, Account
from transactions.models   import Transaction, TransactionType

class TransactionListTest(TestCase):
    def setUp(self):
        password = 'testpassword2@'
        user = User.objects.create(
            id       = 1,
            name     = 'test_user',
            email    = 'test@gmail.com',
            password = password #bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
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
        created_at1 = Transaction.objects.get(id=1).created_at
        created_at2 = Transaction.objects.get(id=2).created_at
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?start-date={date.today()}&end-date={date.today()}',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'ORDER_CAN_NOT_BE_EMPTY'})

    def test_transaction_list_empty_date_range_fail(self):
        created_at1 = Transaction.objects.get(id=1).created_at
        created_at2 = Transaction.objects.get(id=2).created_at
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?order=created_at',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'DATE_RANGE_CAN_NOT_BE_EMPTY'})

    def test_transaction_list_invalid_date_range_fail(self):
        created_at1 = Transaction.objects.get(id=1).created_at
        created_at2 = Transaction.objects.get(id=2).created_at
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?start-date={date.today()}&end-date={date.today()-timedelta(days=1)}&order=created_at',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'INVALID_DATE_RANGE'})

    def test_transaction_list_value_error_fail(self):
        created_at1 = Transaction.objects.get(id=1).created_at
        created_at2 = Transaction.objects.get(id=2).created_at
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?start-date={date.today()}&end-date=wrong!!!!&order=create_at',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'VALUE_ERROR'})

    def test_transaction_list_field_error_fail(self):
        created_at1 = Transaction.objects.get(id=1).created_at
        created_at2 = Transaction.objects.get(id=2).created_at
                
        client   = Client()
        headers  = {'HTTP_Authorization' : self.access_token}
        response = client.get(f'/transactions?start-date={date.today()}&end-date={date.today()}&order=wrong!!!!',
                              **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message':'FIELD_ERROR'})