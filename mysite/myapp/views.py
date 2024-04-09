from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.urls import reverse
from django.db.models import Sum
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
   #Get Expense Name, Amount, Category From User & Save them 
  if request.method == "POST":
    expense = ExpenseForm(request.POST)
    if expense.is_valid():
        expense.instance = expense.save(commit=False)
        expense.instance.user_name = request.user
        expense.instance.save()
        # Redirect to index page after form submission to prevent 
        # the form from being resubmitted on page refresh
        return redirect('myapp:index')
  
  # Get all expenses from Expense Model
  expenses = Expense.objects.filter(user_name=request.user)
  
  # Calculate sum of all expenses
  total_expenses = expenses.aggregate(Sum('amount'))

  # Calculate sum of expenses in last 365 days
  last_year = datetime.date.today() - datetime.timedelta(days=365)
  yearly_sum = expenses.filter(date__gt=last_year).aggregate(Sum('amount'))
  


  # Calculate sum of expenses in last 30 days
  last_month = datetime.date.today() - datetime.timedelta(days=30)
  monthly_sum = expenses.filter(date__gt=last_month).aggregate(Sum('amount'))
  


  # Calculate sum of expenses in last 7 days
  last_week = datetime.date.today() - datetime.timedelta(days=7)
  weekly_sum = expenses.filter(date__gt=last_week).aggregate(Sum('amount'))

  # Calculate sum of expenses made on same date
  sum_of_daily_expenses = expenses.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
  

  # Calculate sum of expenses based on categories
  categorical_sums = expenses.filter().values('category').order_by('category').annotate(sum=Sum('amount'))

  # Render Expense Form to take inputs from user
  expense_form = ExpenseForm()

  return render(request, 'myapp/index.html', {'expense_form':expense_form, 'expenses':expenses, 'total_expenses':total_expenses, 'yearly_sum':yearly_sum, 'monthly_sum':monthly_sum, 'weekly_sum':weekly_sum, 'sum_of_daily_expenses':sum_of_daily_expenses, 'categorical_sums':categorical_sums})

# Handle EDIT Expense Functionality
def edit(request,id):
   expense = Expense.objects.get(id=id)
   expense_form = ExpenseForm(instance=expense)

   # Save data recieved from expense form
   if request.method == "POST":
       expense = Expense.objects.get(id=id)
       form = ExpenseForm(request.POST, instance=expense)
       if form.is_valid():
          form.save()
          # Redirect to index page after form editing
          return redirect('myapp:index')
       
   return render(request, 'myapp/edit.html', { 'expense_form':expense_form } )

# Handle DELETE Expense Functionality
def delete(request, id):
  if request.method == "POST" and 'delete' in request.POST:
    expense = Expense.objects.get(id=id)
    expense.delete()
  return redirect('myapp:index')

