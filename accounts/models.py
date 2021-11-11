from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel):
    email    = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    name     = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'users'

class Account(TimeStampModel):
    number  = models.CharField(max_length=50)
    balance = models.PositiveIntegerField(default=0)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'accounts'