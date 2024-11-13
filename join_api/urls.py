from django.urls import path
from .views import save_item, get_item, Contacts

urlpatterns = [
    path('save_item/', save_item),
    path('get_item/<str:key>/', get_item),
    path('contact/', Contacts)
]

