from django.urls import path

from common import views

app_name = 'common'
urlpatterns = [
    path('health-check/', views.health_check, name='health-check')
]
