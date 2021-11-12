from django.db       import models

from core.models     import TimeStampModel
from accounts.models import Account

class TransactionType(TimeStampModel):
    
    class Name(models.IntegerChoices):
        DEPOSIT  = 1
        WITHDRAW = 2
    
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'transaction_types'

class Transaction(models.Model):
    amount                    = models.PositiveIntegerField()
    balance_after_transaction = models.PositiveIntegerField()
    sum_up                    = models.CharField(max_length=100)
    account                   = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type          = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    created_at                = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'transactions'