from django.urls import path
from dashboard import views

urlpatterns = [
    
    path('dashboard/', views.index, name='dashboard-index'),
    path('home/', views.home, name='dashboard-home'),
    path('contact/', views.contact, name='dashboard-contact'),
        path('about/', views.about, name='dashboard-about'),

    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staffDetail'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.productDelete, name='dashboard-productDelete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-productUpdate'),                   
    path('order/', views.order, name='dashboard-order'),
]  

