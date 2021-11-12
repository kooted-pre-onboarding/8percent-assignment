import json
from django.core.checks.messages import Info

from django.views   import View
from django.http    import JsonResponse
from django.views.generic.base import TemplateView

from accounts.models import Account
from accounts.utils  import login_decorator

from transactions.models import Transaction, TransactionType


class DepositTransactionView(TemplateView):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            account = Account.objects.get(user_id = user.id)

            if data["amount"] <= 0:
                return JsonResponse({"message" : "INVALID_INPUT"}, status=400)
        
            account.balance += data["amount"]
            account.save()

            Transaction.objects.create(
                transaction_type_id       = TransactionType.Name.DEPOSIT.value,
                amount                    = int(data["amount"]),
                account_id                = account.id,
                balance_after_transaction = account.balance,
                sum_up                    = data["sum_up"])
    
            return JsonResponse(
                {"message": "SUCCESS", "deposit_balance": account.balance}, status=201)

        except TypeError:
            return JsonResponse({"message": "TYPE_ERROR"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class WithdrawTransactionlView(TemplateView):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            account = Account.objects.get(user_id = user.id)

            if data["amount"] <= 0:
                return JsonResponse({"message": "INVALID_INPUT"}, status=400)

            if data["amount"] > account.balance:
                return JsonResponse({"message": "WRONG_REQUEST"}, status=400)
            
            account.balance -= data["amount"]
            account.save()

            Transaction.objects.create(
                transaction_type_id       = TransactionType.Name.WITHDRAW.value,
                amount                    = data["amount"],
                account_id                = account.id,
                balance_after_transaction = account.balance,
                sum_up                    = data["sum_up"])

            return JsonResponse(
                {"message": "SUCCESS", "deposit_balance": account.balance}, status=201)

        except TypeError:
            return JsonResponse({"message": "TYPE_ERROR"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)