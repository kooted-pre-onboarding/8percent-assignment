from django.urls import path

from transactions.views import DepositTransactionView, WithdrawTransactionlView

urlpatterns = [
    path('/deposit', DepositTransactionView.as_view()),
    path('/withdraw', WithdrawTransactionlView.as_view())
]