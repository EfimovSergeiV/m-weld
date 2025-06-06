"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from .views import CategoryView, ProductsView, ProductView

urlpatterns = [
    path('cts/', CategoryView.as_view(), name='categories'),
    path('cts/<int:ct>/', CategoryView.as_view(), name='categories'),
    path('prods/<int:ct>/', ProductsView.as_view(), name='products'),
    path('prod/<int:id>/', ProductView.as_view(), name='product'),
]
