from django.forms import ModelForm
from .models import Expense


'''
  'ExpenseForm' is a model form inherited from ModelForm
'''
class ExpenseForm(ModelForm):
  class Meta:
    # Expense is the model used by this class
    model = Expense
    # Fields in Expense Form
    fields = ('name','amount','category')

