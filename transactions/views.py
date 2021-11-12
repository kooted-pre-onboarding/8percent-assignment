import json
from django.core.checks.messages import Info

from django.views   import View
from django.http    import JsonResponse
from django.views.generic.base import TemplateView

from accounts.models import Account

from transactions.models import Transaction, TransactionType


class DepositTransactionView(TemplateView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            # user = request.user
            account = Account.objects.get(user_id = 1)
            type_id = TransactionType.objects.get(type_id = 1)

            print(type_id)
            if data["amount"] <= 0:
                return JsonResponse({"message" : "INVALID_INPUT"}, status=400)
        
            account.balance += data["amount"]
            account.save()

            Transaction.objects.create(
                type_id = type_id,
                amount=int(data["amount"]),
                account_id = account.id,
                balance_after_transaction = account.balance,
                sum_up = data["sum_up"])
    
            return JsonResponse(
                {"message": "SUCCESS", "deposit_balance": account.balance}, status=201)

        # except TypeError:
        #     return JsonResponse({"message": "TYPE_ERROR"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class WithdrawTransactionlView(TemplateView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            #user = request.user
            account = Account.objects.filter(user_id = 1)

            if data["amount"] <= 0:
                return JsonResponse({"message": "INVALID_INPUT"}, status=400)

            if data["amounts"] > account.amount:
                return JsonResponse({"message": "WRONG_REQUEST"}, status=400)

            account = Account.objects.select_related('number')
            
            account.amount -= data["amounts"]
            account.save()

            Transaction.objects.create(
                type = data['type'],
                amount = data["amount"],
                account_id = account.id,
                balance_after_transaction = account.balance,
                sum_up = data["sum_up"])

            return JsonResponse(
                {"message": "SUCCESS", "deposit_balance": account.balance}, status=201)

        except TypeError:
            return JsonResponse({"message": "TYPE_ERROR"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)