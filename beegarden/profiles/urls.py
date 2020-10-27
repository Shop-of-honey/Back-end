from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from profiles.views import ProductsViewSet, UserListView, ProductListView

profiles_router = DefaultRouter()
profiles_router.register(r'', ProductsViewSet, basename='profiles')

user_router = DefaultRouter()
user_router.register(r'', UserListView, basename='profiles')

app_name = 'profiles'
urlpatterns = [
    re_path(r'user/(?P<search_string>\w+|)', UserListView.as_view()),
    re_path(r'product/(?P<search_string>\w+|)', ProductListView.as_view()),
    re_path(r'products/', include(profiles_router.urls)),
]
