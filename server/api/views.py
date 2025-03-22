from django.shortcuts import render

# Create your views here.
# /server/api/views.py
from django.shortcuts import render, redirect
from .models import User, FarmerProfile, CertificationRequest, Category, Product, Order, Payment, Review, FAQ, ContactForm, Blog
from .forms import UserForm, FarmerProfileForm, CertificationRequestForm, CategoryForm, ProductForm, OrderForm, PaymentForm, ReviewForm, FAQForm, ContactFormForm, BlogForm

# View to add a new User
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_user')  # Redirect to the same page or another page
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

# View to add a new FarmerProfile
def add_farmer_profile(request):
    if request.method == 'POST':
        form = FarmerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_farmer_profile')
    else:
        form = FarmerProfileForm()
    return render(request, 'add_farmer_profile.html', {'form': form})

# View to add a new CertificationRequest
def add_certification_request(request):
    if request.method == 'POST':
        form = CertificationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_certification_request')
    else:
        form = CertificationRequestForm()
    return render(request, 'add_certification_request.html', {'form': form})

# View to add a new Category
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

# View to add a new Product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# View to add a new Order
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_order')
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

# View to add a new Payment
def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_payment')
    else:
        form = PaymentForm()
    return render(request, 'add_payment.html', {'form': form})

# View to add a new Review
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_review')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

# View to add a new FAQ
def add_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_faq')
    else:
        form = FAQForm()
    return render(request, 'add_faq.html', {'form': form})

# View to add a new ContactForm
def add_contact_form(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_contact_form')
    else:
        form = ContactFormForm()
    return render(request, 'add_contact_form.html', {'form': form})

# View to add a new Blog
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_blog')
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})
