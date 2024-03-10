"""
URL configuration for CRUDOpsByDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# inventory/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showDashboard, name="showDashboard"),  # This URL path is '/'
    path('dashboard/', views.showDashboard2, name="showDashboard2"),
    path('showProducts/', views.showProducts, name="showProducts"),  # This is a different path
    path('InsertUser/', views.InsertUser, name="InsertUser"),
    path('producthistory/<int:id>/<int:users_id>/', views.Phistory, name="Phistory"),
    path('InsertProductDetails/<int:users_id>', views.InsertProductDetails, name="InsertProductDetails"),
    path('showProductDetails/<int:users_id>/', views.showProductDetails1, name="showProductDetails"),
    path('addedProductDetails/<int:users_id>/', views.addedProductDetails, name="addedProductDetails"),
    path('EditProducts/<int:id>/<int:users_id>', views.EditProduct, name='EditProduct'),
    path('UpdateProducts/<int:id>/<int:users_id>', views.UpdateProducts, name="UpdateProducts"),
    path('DeleteProducts/<int:id>/<int:users_id>', views.DelProduct, name="DelProduct"),
]
