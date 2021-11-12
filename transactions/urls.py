from django.urls import path

from .views      import DepositView, WithdrawView, TransactionListView

urlpatterns = [
    path('/deposit', DepositView.as_view()),
    path('/withdraw', WithdrawView.as_view()),
    path('', TransactionListView.as_view()),
]
