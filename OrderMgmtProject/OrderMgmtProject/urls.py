"""
URL configuration for OrderMgmtProject project.

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
from django.contrib import admin
from django.urls import path
from OrderMgmtApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('OrderMgmt/index/', views.index, name='index'),
    path('OrderMgmt/add_customer', views.index, name='create_contact_from_customer'),
    path('OrderMgmt/editCustomer/<int:id>/', views.EditCustomerView.as_view(), name='edit_customer'),
    path('OrderMgmt/createModelContact/<int:fk>/', views.createContactFromModelForm, name='create_model_contact'),
    path('OrderMgmt/editModelContact/<int:id>/', views.EditContactView.as_view(), name='edit_model_contact'),

]
'''
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from OrderMgmtApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('OrderMgmt/index/', views.index, name='index'),
]
'''
