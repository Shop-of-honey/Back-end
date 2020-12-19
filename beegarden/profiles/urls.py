from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
from profiles import views

from profiles.views import UserListView, ProductListView, UsersViewSet, ProductList, ProductCreate, ProductUpdate, ProductDelete

users_router = DefaultRouter()
users_router.register(r'', UsersViewSet, basename='users')

app_name = 'profiles'
urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/create', ProductCreate.as_view()),
    path('products/<int:pk>', ProductUpdate.as_view()),
    path('products/<int:pk>/delete',ProductDelete.as_view()),
    re_path(r'usersearch/(?P<search_string>\w+|)', UserListView.as_view()),
    re_path(r'product/(?P<search_string>\w+|)', ProductListView.as_view()),
    re_path(r'users/', include(users_router.urls)),
    path('is_authenticated/', views.is_authenticated, name='is_authenticated')
]
