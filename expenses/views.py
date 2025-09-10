from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import Expense

def index(request):
    """Main page showing expenses list and summary"""
    expenses = Expense.objects.all()
    
    # Calculate totals by category
    category_totals = {}
    total_amount = 0
    
    for category_choice in Expense.CATEGORY_CHOICES:
        category_code = category_choice[0]
        category_name = category_choice[1]
        category_sum = expenses.filter(category=category_code).aggregate(Sum('amount'))['amount__sum'] or 0
        category_totals[category_name] = category_sum
        total_amount += category_sum
    
    context = {
        'expenses': expenses,
        'category_totals': category_totals,
        'total_amount': total_amount,
    }
    return render(request, 'expenses/index.html', context)

def add_expense(request):
    """Add a new expense"""
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        date = request.POST.get('date')
        
        # Basic validation
        if not all([category, amount, description, date]):
            messages.error(request, 'All fields are required.')
            return redirect('index')
        
        try:
            amount = float(amount)
            if amount <= 0:
                messages.error(request, 'Amount must be greater than 0.')
                return redirect('index')
        except ValueError:
            messages.error(request, 'Please enter a valid amount.')
            return redirect('index')
        
        # Create the expense
        Expense.objects.create(
            category=category,
            amount=amount,
            description=description,
            date=date
        )
        
        messages.success(request, 'Expense added successfully!')
        return redirect('index')
    
    return redirect('index')

def delete_expense(request, expense_id):
    """Delete an expense"""
    try:
        expense = Expense.objects.get(id=expense_id)
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
    except Expense.DoesNotExist:
        messages.error(request, 'Expense not found.')
    
    return redirect('index')
