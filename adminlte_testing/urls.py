from django.urls import path
from .views import (
    adminlte_view,
)

app_name = 'adminlte_testing'
urlpatterns = [
    path('', adminlte_view, name='adminlte-starter'),
]
