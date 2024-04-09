from django.db import models
from django.contrib.auth.models import User


# Create your models here.
'''
  'Expense' is a model inherited from models.Model
'''
class Expense(models.Model):
  # Fields in Expense Model
  user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  name = models.CharField(max_length=100)
  amount = models.IntegerField()
  category = models.CharField(max_length=50)
  # 'auto_now' will set date as current date automatically
  date = models.DateField(auto_now=True)

  # Convert Object into a String
  def __str__(self):
    return self.name

 