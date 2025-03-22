# /server/api/forms.py
from django import forms
from .models import User, FarmerProfile, CertificationRequest, Category, Product, Order, Payment, Review, FAQ, ContactForm, Blog

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'password', 'role']

class FarmerProfileForm(forms.ModelForm):
    class Meta:
        model = FarmerProfile
        fields = ['user', 'address', 'city', 'state', 'pincode']

class CertificationRequestForm(forms.ModelForm):
    class Meta:
        model = CertificationRequest
        fields = ['farmer', 'submitted_documents', 'status', 'inspection_date', 'approval_date', 'rejection_reason']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['farmer', 'category', 'product_name', 'description', 'price', 'stock', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'total_price', 'order_status', 'payment_status']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['order', 'payment_method', 'transaction_id', 'payment_status']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['customer', 'product', 'rating', 'comment']

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message', 'status']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author']