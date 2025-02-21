from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Record(models.Model):
    TRANSACTION_TYPE_CHOICES = [('INCOME', "Income"), ('EXPENSE', 'Expense')]
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    transaction_type = models.CharField(max_length=8, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField("Tag", related_name="tags")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)



