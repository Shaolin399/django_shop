from django.shortcuts import render,get_object_or_404
from .models import Product
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    products = Product.objects.all()
    return render(request, 'myshop/index.html', {'products': products})

def contact_us(request):
    return render(request, 'myshop/contact_us.html')

def faq(request):
    return render(request, 'myshop/faq.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Неправильний email або пароль.')
    else:
        form = LoginForm()

    return render(request, 'myshop/login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'myshop/register.html', {'form': form})


def shopping_cart(request):
    return render(request, 'myshop/shopping_cart.html')

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'myshop/product_detail.html', {'product': product})

def filter_options(request):
    brands = Product.objects.values_list('brand', flat=True).distinct()
    memories = Product.objects.values_list('memory', flat=True).distinct()
    batteries = Product.objects.values_list('battery_capacity', flat=True).distinct()
    storage_capacities = Product.objects.values_list('storage_capacity', flat=True).distinct()
    camera_resolutions = Product.objects.values_list('camera_resolution', flat=True).distinct()

    return JsonResponse({
        'brands': list(brands),
        'memories': list(memories),
        'batteries': list(batteries),
        'storageCapacities': list(storage_capacities),
        'cameraResolutions': list(camera_resolutions),
    })
