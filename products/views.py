from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.decorators.http import require_POST

def home(request):
    return render(request, 'products/home.html')


def add_product(request):

    submitted_product = None

    if request.method == 'POST':

        form = ProductForm(request.POST)

        if form.is_valid():

            # Save the product to the database
            submitted_product = form.save()

            # Reset the form
            form = ProductForm()

    else:

        form = ProductForm()

    return render(request, 'products/add_product.html', {
        'form': form,
        'submitted_product': submitted_product,
    })

def product_list(request):

    products = Product.objects.all().order_by('-id')

    return render(request, 'products/product_list.html', {
        'products': products
    })

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = UserCreationForm()

    return render(request, 'products/register.html', {
        'form': form
    })

def user_login(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')

    else:

        form = AuthenticationForm(request)

    return render(request, 'products/login.html', {
        'form': form
    })

@require_POST
def user_logout(request):

    logout(request)

    return redirect('home')