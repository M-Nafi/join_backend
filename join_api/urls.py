from django.urls import path
from .views import ContactcreateView, ContactListView, ContactDetailView, ContactDeleteView, TaskCreateView, TaskListView
 
urlpatterns = [
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('add_contact/', ContactcreateView.as_view(), name='add-contact'),  # POST zum Hinzufügen von Kontakten
    path('contacts/', ContactListView.as_view(), name='contact-list'),  # GET zum Abrufen der Kontakte
    path('contacts/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
    path('add_task/', TaskCreateView.as_view(), name='add-list'),
    path('tasks/', TaskListView.as_view(), name='task-list')
]
