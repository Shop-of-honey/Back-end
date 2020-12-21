from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
from profiles import views

from profiles.views import UserListView, ProductListView, ProductList, ProductCreate, ProductUpdate, \
                           ProductDelete, UserList, UserCreate, UserUpdate, UserDelete

app_name = 'profiles'
urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/create', ProductCreate.as_view()),
    path('products/<int:pk>', ProductUpdate.as_view()),
    path('products/<int:pk>/delete',ProductDelete.as_view()),
    path('users', UserList.as_view()),
    path('users/create', UserCreate.as_view()),
    path('users/<int:pk>', UserUpdate.as_view()),
    path('users/<int:pk>/delete', UserDelete.as_view()),
    re_path(r'usersearch/(?P<search_string>\w+|)', UserListView.as_view()),
    re_path(r'product/(?P<search_string>\w+|)', ProductListView.as_view()),
    path('is_authenticated/', views.is_authenticated, name='is_authenticated')
]
