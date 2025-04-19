from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Expense, Category, CustomUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = make_password(request.POST['password'])
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            CustomUser.objects.create(username=username, email=email, password=password)
            return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Username:", username)
        print("Password:", password)

        user = authenticate(request,username = username,password = password)
        if user:
            login(request,user)
            return redirect('expense-list')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    context = {'expenses' : expenses}
    return render(request,'expense_list.html',context)


@login_required
def expense_create(request):
    categories = Category.objects.filter(user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        notes = request.POST.get('notes')
        category_id = request.POST.get('category')
        new_category_name = request.POST.get('new_category').strip()  # Get the new category name

        if category_id == "__new__" and new_category_name:
            # Create a new category if the user selected "Add New Category"
            category = Category.objects.create(name=new_category_name, user=request.user)
        else:
            # Fetch the selected category
            category = Category.objects.filter(id=category_id, user=request.user).first()

        # Create the expense and associate the category
        Expense.objects.create(user=request.user, title=title, amount=amount, date=date, notes=notes, category=category)
        return redirect('expense-list')
    
    return render(request, 'expense_form.html', {'categories': categories})


@login_required
def expense_update(request, pk):
    expense = Expense.objects.get(id=pk, user=request.user)
    categories = Category.objects.filter(user=request.user)
    
    if request.method == 'POST':
        expense.title = request.POST.get('title')
        expense.amount = request.POST.get('amount')
        expense.date = request.POST.get('date')
        expense.notes = request.POST.get('notes')
        category_id = request.POST.get('category')
        new_category_name = request.POST.get('new_category').strip()  # Get the new category name

        if category_id == "__new__" and new_category_name:
            # Create a new category if the user selected "Add New Category"
            category = Category.objects.create(name=new_category_name, user=request.user)
        else:
            # Fetch the selected category
            category = Category.objects.filter(id=category_id, user=request.user).first()

        # Update the expense with the selected or new category
        expense.category = category
        expense.save()

        return redirect('expense-list')

    return render(request, 'expense_form.html', {'expense': expense, 'categories': categories})


@login_required
def expense_delete(request, pk):
    expense = Expense.objects.get(id=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense-list')
    return render(request, 'core/expense_confirm_delete.html', {'expense': expense})