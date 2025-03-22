from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
    path('dashboard/farmer/', views.farmer_dashboard, name='farmer_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/verifier/', views.verifier_dashboard, name='verifier_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  
   
    
    path('', views.index_view, name='home'),
]
