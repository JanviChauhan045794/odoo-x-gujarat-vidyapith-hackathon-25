from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .forms import UserSignupForm, ProductForm, FarmerProfileForm, CustomerProfileForm
from .models import FarmerProfile, CertificationRequest, User, Product, Category, CustomerProfile
from .serializers import ProductSerializer, CategorySerializer


def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')  
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard_view(request):
    if request.user.role == 'Customer':
        return redirect('customer_dashboard')
    elif request.user.role == 'Farmer':
        return redirect('farmer_dashboard')
    elif request.user.role == 'Admin':
        return redirect('admin_dashboard')
    elif request.user.role == 'Verifier':
        return redirect('verifier_dashboard')
    else:
        messages.error(request, "Invalid user role.")
        return redirect('home')  # Redirect to home if the role is invalid

@login_required
def customer_dashboard(request):
    if request.user.role != 'Customer':
        messages.error(request, 'Only customers can access this dashboard.')
        return redirect('home')
    
    try:
        customer_profile = CustomerProfile.objects.get(user=request.user)
    except CustomerProfile.DoesNotExist:
        customer_profile = None
    
    context = {
        'customer_profile': customer_profile,
    }
    return render(request, 'customer/customer_dashboard.html', context)

@login_required
def farmer_dashboard(request):
    if request.user.role != 'Farmer':
        messages.error(request, 'Only farmers can access this dashboard.')
        return redirect('home')
    
    try:
        farmer_profile = FarmerProfile.objects.get(user=request.user)
        recent_products = Product.objects.filter(farmer=farmer_profile).order_by('-created_at')[:5]
    except FarmerProfile.DoesNotExist:
        farmer_profile = None
        recent_products = []
    
    context = {
        'farmer_profile': farmer_profile,
        'recent_products': recent_products,
    }
    return render(request, 'farmer/farmer_dashboard.html', context)

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def verifier_dashboard(request):
    return render(request, 'verifier/verifier_dashboard.html')

def index_view(request):
    return render(request, 'index.html')

@login_required
def add_product(request):
    # Check if user is a farmer
    if request.user.role != 'Farmer':
        messages.error(request, 'Only farmers can add products.')
        return redirect('product_list')

    try:
        farmer_profile = FarmerProfile.objects.get(user=request.user)
    except FarmerProfile.DoesNotExist:
        messages.error(request, 'Please complete your farmer profile before adding products.')
        return redirect('farmer_dashboard')

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

@login_required
def edit_product(request, product_id):
    # Check if user is a farmer
    if request.user.role != 'Farmer':
        messages.error(request, 'Only farmers can edit products.')
        return redirect('product_list')

    try:
        farmer_profile = FarmerProfile.objects.get(user=request.user)
        product = get_object_or_404(Product, id=product_id, farmer=farmer_profile)
    except (FarmerProfile.DoesNotExist, Product.DoesNotExist):
        messages.error(request, 'Product not found or you do not have permission to edit it.')
        return redirect('product_list')

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            try:
                product = form.save(commit=False)
                product.farmer = farmer_profile
                
                # Handle image upload
                if 'image' in request.FILES:
                    product.image = request.FILES['image']
                
                product.save()
                messages.success(request, 'Product updated successfully!')
                return redirect('product_list')
            except Exception as e:
                messages.error(request, f'Error updating product: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
        'farmer': farmer_profile,
        'categories': Category.objects.all(),
    }
    return render(request, 'edit_product.html', context)

@login_required
def delete_product(request, product_id):
    # Check if user is a farmer
    if request.user.role != 'Farmer':
        messages.error(request, 'Only farmers can delete products.')
        return redirect('product_list')

    try:
        farmer_profile = FarmerProfile.objects.get(user=request.user)
        product = get_object_or_404(Product, id=product_id, farmer=farmer_profile)
        product.delete()
        messages.success(request, 'Product deleted successfully!')
    except (FarmerProfile.DoesNotExist, Product.DoesNotExist):
        messages.error(request, 'Product not found or you do not have permission to delete it.')
    
    return redirect('product_list')

# Product List View
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories
    })

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

@login_required
def edit_farmer_profile(request):
    if request.user.role != 'Farmer':
        messages.error(request, 'Only farmers can edit their profile.')
        return redirect('home')
    
    try:
        farmer_profile = FarmerProfile.objects.get(user=request.user)
    except FarmerProfile.DoesNotExist:
        farmer_profile = None
    
    if request.method == 'POST':
        form = FarmerProfileForm(request.POST, instance=farmer_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('farmer_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FarmerProfileForm(instance=farmer_profile)
    
    context = {
        'form': form,
        'farmer_profile': farmer_profile,
    }
    return render(request, 'farmer/edit_profile.html', context)

@login_required
def edit_customer_profile(request):
    if request.user.role != 'Customer':
        messages.error(request, 'Only customers can edit their profile.')
        return redirect('home')
    
    try:
        customer_profile = CustomerProfile.objects.get(user=request.user)
    except CustomerProfile.DoesNotExist:
        customer_profile = None
    
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES, instance=customer_profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('customer_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerProfileForm(instance=customer_profile)
    
    context = {
        'form': form,
        'customer_profile': customer_profile,
    }
    return render(request, 'customer/edit_profile.html', context)

@login_required
def certification_request(request):
    if request.user.role != 'Farmer':
        messages.error(request, 'Only farmers can request certification.')
        return redirect('home')
    
    try:
        farmer_profile = FarmerProfile.objects.get(user=request.user)
        certification_requests = CertificationRequest.objects.filter(farmer=farmer_profile).order_by('-submitted_at')
    except FarmerProfile.DoesNotExist:
        messages.error(request, 'Please complete your farmer profile first.')
        return redirect('farmer_dashboard')
    
    if request.method == 'POST':
        if 'submitted_documents' in request.FILES:
            CertificationRequest.objects.create(
                farmer=farmer_profile,
                submitted_documents=request.FILES['submitted_documents']
            )
            messages.success(request, 'Certification request submitted successfully!')
            return redirect('certification_request')
        else:
            messages.error(request, 'Please upload your documents.')
    
    context = {
        'certification_requests': certification_requests,
        'farmer_profile': farmer_profile,
    }
    return render(request, 'farmer/certification_request.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


