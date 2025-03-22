# /server/api/urls.py
from django.urls import path
from .views import (
    add_user, add_farmer_profile, add_certification_request, 
    add_category, add_product, add_order, add_payment, 
    add_review, add_faq, add_contact_form, add_blog
)

urlpatterns = [
    path('add_user/', add_user, name='add_user'),
    path('add_farmer_profile/', add_farmer_profile, name='add_farmer_profile'),
    path('add_certification_request/', add_certification_request, name='add_certification_request'),
    path('add_category/', add_category, name='add_category'),
    path('add_product/', add_product, name='add_product'),
    path('add_order/', add_order, name='add_order'),
    path('add_payment/', add_payment, name='add_payment'),
    path('add_review/', add_review, name='add_review'),
    path('add_faq/', add_faq, name='add_faq'),
    path('add_contact_form/', add_contact_form, name='add_contact_form'),
    path('add_blog/', add_blog, name='add_blog'),
]