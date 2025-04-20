from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import Expense, Category, CustomUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponse

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = make_password(request.POST['password'])
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            CustomUser.objects.create(username=username, email=email, password=password)
            messages.success(request, 'Registered Successfully.')
            return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    # If the user is already authenticated, redirect to expense-list
    if request.user.is_authenticated:
        return redirect('expense-list')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Username:", username)
        print("Password:", password)

        user = authenticate(request,username = username,password = password)
        if user:
            login(request,user)
            messages.success(request, 'Logged In Successfully!')
            return redirect('expense-list')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('login')
    return render(request, 'logout_confirm.html')

def index(request):
    return render(request,'home.html')

def expense_list(request):
    # If the user is not logged in, redirect to the login page with a message
    if not request.user.is_authenticated:
        messages.warning(request, 'You must be logged in to view your expenses.')
        return redirect('login')
    
    expenses = Expense.objects.filter(user=request.user)
    context = {'expenses': expenses}
    return render(request, 'expense_list.html', context)



def expense_create(request):
    # If the user is not logged in, redirect to the login page with a message
    if not request.user.is_authenticated:
        messages.warning(request, 'You must be logged in to create your expenses.')
        return redirect('login')
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
        messages.success(request, 'Expense Created Successfully!')
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
        messages.success(request, 'Expense Updated Successfully!')
        return redirect('expense-list')

    return render(request, 'expense_form.html', {'expense': expense, 'categories': categories})


@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, id=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense Deleted Successfully!')
        return redirect('expense-list')
    return render(request, 'expense_confirm_delete.html', {'expense': expense})