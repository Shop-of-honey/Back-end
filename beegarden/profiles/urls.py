from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from profiles.views import ProductsViewSet, UserListView, ProductListView, UsersViewSet

profiles_router = DefaultRouter()
profiles_router.register(r'', ProductsViewSet, basename='profiles')

users_router = DefaultRouter()
users_router.register(r'', UsersViewSet, basename='users')

app_name = 'profiles'
urlpatterns = [
    re_path(r'usersearch/(?P<search_string>\w+|)', UserListView.as_view()),
    re_path(r'product/(?P<search_string>\w+|)', ProductListView.as_view()),
    re_path(r'products/', include(profiles_router.urls)),
    re_path(r'users/', include(users_router.urls)),
]
