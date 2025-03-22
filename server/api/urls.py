from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
    path('dashboard/farmer/', views.farmer_dashboard, name='farmer_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/verifier/', views.verifier_dashboard, name='verifier_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.index_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    
    # Product-related URLs
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    
    # Farmer Profile URLs
    path('farmer/profile/edit/', views.edit_farmer_profile, name='edit_farmer_profile'),
    path('customer/profile/edit/', views.edit_customer_profile, name='edit_customer_profile'),
    path('farmer/certification/', views.certification_request, name='certification_request'),
    
    # Verifier URLs
    path('certification/update/<int:request_id>/', views.update_certification_status, name='update_certification_status'),
    
    # API URLs
    path('api/', include(router.urls)),
]
