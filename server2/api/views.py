from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .forms import UserSignupForm, ProductForm
from .models import Product, FarmerProfile, Category, User
from .serializers import ProductSerializer, CategorySerializer

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            # Create user
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                full_name=form.cleaned_data['full_name'],
                phone_number=form.cleaned_data['phone_number'],
                password=form.cleaned_data['password'],
                role=form.cleaned_data['role']
            )
            
            # If user is a farmer, create farmer profile
            if form.cleaned_data['role'] == 'Farmer':
                FarmerProfile.objects.create(
                    user=user,
                    address='',  # These can be updated later
                    city='',
                    state='',
                    pincode=''
                )
            
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

# Dashboard View (Temporarily No Login Required)
def dashboard_view(request):
    return render(request, 'dashboard.html')

# Homepage
def index_view(request):
    return render(request, 'index.html')

# Logout Success Page
def logout_success_view(request):
    return render(request, 'logout_success.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')  # Form field name is 'username'
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                messages.success(request, f'Welcome back {user.full_name}!')
                if user.role == 'Farmer':
                    return redirect('add_product')
                return redirect('product_list')
        except User.DoesNotExist:
            pass
        
        messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

@login_required
def add_product(request):
    # Check if user is a farmer
    if request.user.role != 'Farmer':
        messages.error(request, 'Only farmers can add products.')
        return redirect('product_list')

    try:
        farmer_profile = FarmerProfile.objects.get(user=request.user)
    except FarmerProfile.DoesNotExist:
        # Create farmer profile if it doesn't exist
        farmer_profile = FarmerProfile.objects.create(
            user=request.user,
            address='',
            city='',
            state='',
            pincode=''
        )

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                product = form.save(commit=False)
                product.farmer = farmer_profile
                
                # Handle image upload
                if 'image' in request.FILES:
                    product.image = request.FILES['image']
                
                product.save()
                messages.success(request, 'Product added successfully!')
                return redirect('product_list')
            except Exception as e:
                messages.error(request, f'Error saving product: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
            print("Form errors:", form.errors)  # Debug print
    else:
        form = ProductForm()
    
    # Get available categories for debugging
    categories = Category.objects.all()
    print("Available categories:", categories)  # Debug print
    
    context = {
        'form': form,
        'farmer': farmer_profile,
        'categories': categories,  # Add categories to context
    }
    return render(request, 'add_product.html', context)

# Product List View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# REST API Views
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'farmer']
    search_fields = ['product_name', 'description']
    ordering_fields = ['price', 'created_at']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        try:
            farmer_profile = FarmerProfile.objects.get(user=self.request.user)
            serializer.save(farmer=farmer_profile)
        except FarmerProfile.DoesNotExist:
            return Response(
                {"error": "Only farmers can create products"},
                status=status.HTTP_403_FORBIDDEN
            )

    @action(detail=False, methods=['get'])
    def my_products(self, request):
        try:
            farmer_profile = FarmerProfile.objects.get(user=request.user)
            products = self.queryset.filter(farmer=farmer_profile)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        except FarmerProfile.DoesNotExist:
            return Response(
                {"error": "Farmer profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
