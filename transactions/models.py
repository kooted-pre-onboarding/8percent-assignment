from django.db       import models

from core.models     import TimeStampModel
from accounts.models import Account

class TransactionType(TimeStampModel):
    type = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'transaction_types'

class Transaction(TimeStampModel):
    amount                    = models.PositiveIntegerField()
    balance_after_transaction = models.PositiveIntegerField()
    sum_up                    = models.CharField(max_length=100)
    account                   = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type          = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'transactions'