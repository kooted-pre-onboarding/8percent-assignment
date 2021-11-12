import jwt

from django.http            import JsonResponse

from eightpercent.settings  import SECRET_KEY, ALGORITHM
from .models                import User

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers: 
            return JsonResponse ({'message' : 'UNAUTHORIZED'}, status=401)

        access_token = request.headers.get('Authorization')
        
        try:
            payload      = jwt.decode(access_token, SECRET_KEY, algorithms=ALGORITHM)
            user         = User.objects.get(id=payload['user_id'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE': 'INVALID_TOKEN'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)

        return func(self, request,  *args, **kwargs)

    return wrapper