import json
from datetime               import datetime, timedelta

from django.http            import JsonResponse
from django.views           import View
from django.db.models       import Q
from django.core.exceptions import FieldError

from transactions.models    import Transaction
from accounts.models        import Account
from accounts.utils         import login_decorator

class TransactionListView(View):
    @login_decorator
    def get(self, request):
        try:
            user = request.user
            
            if not Account.objects.filter(user=user.id).exists():
                return JsonResponse({'message':'ACCOUNT_DOES_NOT_EXIST'}, status=404)
            
            account = Account.objects.get(user_id=user.id)
            
            start_date = request.GET.get('start-date', None)
            end_date   = request.GET.get('end-date', None)
            type       = request.GET.get('type', None)
            order      = request.GET.get('order', None)
            offset     = int(request.GET.get('offset', 0))
            limit      = int(request.GET.get('limit', 50))
            
            if not order:
                return JsonResponse({'message':'ORDER_CAN_NOT_BE_EMPTY'}, status=400)

            if not (start_date and end_date):
                return JsonResponse({'message':'DATE_RANGE_CAN_NOT_BE_EMPTY'}, status=400)
            
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date   = datetime.strptime(end_date, '%Y-%m-%d')
            
            if end_date < start_date:
                return JsonResponse({"message":"INVALID_DATE_RANGE"}, status=400)
            
            if (start_date == end_date):
                end_date += timedelta(days=1)

            q = Q()
            q &= Q(created_at__range=(start_date, end_date))
            
            if type:
                q &= Q(transaction_type__type=type)        
            
            transactions = Transaction.objects.filter(q, account_id=account.id).order_by(order)[offset:offset+limit]

            data = [{
                'datetime' : datetime.strftime(transaction.created_at,'%Y-%m-%d %H:%M:%S'),
                'amount'   : transaction.amount,
                'balance'  : transaction.balance_after_transaction,
                'type'     : transaction.transaction_type.name,
                'sum_up'   : transaction.sum_up
            } for transaction in transactions]

            return JsonResponse({'data': data}, status=200)

        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)
        except FieldError:
            return JsonResponse({'message':'FIELD_ERROR'}, status=400)