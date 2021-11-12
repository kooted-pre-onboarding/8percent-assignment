import json, re, bcrypt, jwt, random
from json.decoder           import JSONDecodeError

from django.http            import JsonResponse
from django.views           import View
from django.db              import transaction

from accounts.models        import User, Account
from eightpercent.settings  import SECRET_KEY, ALGORITHM

class SignUp(View):
    @transaction.atomic
    def post(self, request):
        data          = json.loads(request.body)
        REGX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        REGX_PASSWORD = '^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$'

        try:
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'EXIST_EMAIL'}, status=400)

            if not re.match(REGX_EMAIL, data['email']):
                return JsonResponse({'message': 'INVALID_EMAIL_FORM'}, status=400)

            if not re.match(REGX_PASSWORD, data['password']):
                return JsonResponse({'message': 'INVALID_PASSWORD_FORM'}, status=400)

            password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # 고유한 신규계좌 발급 / 기존 생성된 계좌번호들과 중복 방지를 위한 대조
            def Account_number():
                def numbers():
                    number = random.randint(1000, 9999)
                    return number

                account_number = f'{numbers()}-{numbers()}-{numbers()}-{numbers()}'
                
                if not Account.objects.filter(number=account_number).exists():
                   return account_number

                return Account_number()
            
            user = User.objects.create(
                name     = data['name'],
                email    = data['email'],
                password = password,
            )

            Account.objects.create(
                number  = Account_number(),
                user_id = user.id
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class SignIn(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message' : 'INVALID_USER'}, status=401)

            user = User.objects.get(email=data['email'])

            if not (user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8'))):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=401)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        access_token = jwt.encode({'user_id' : user.id}, SECRET_KEY, ALGORITHM)

        return JsonResponse({'access_token' : access_token}, status=200)
