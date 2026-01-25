from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ("INCOME", "Income"),
        ("EXPENSE", "Expense"),
    )

    MONEY_TYPE = (
        ("HAND CASH", "Hand Cash"),
        ("UPI CASH", "UPI Cash")
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    money_type = models.CharField(max_length=20, choices=MONEY_TYPE, default="HAND CASH")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - ₹{self.amount}"
