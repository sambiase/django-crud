from django.urls import path
from .views import read, delete, create, edit, update

urlpatterns = [
    path('', read),
    path('delete/<int:id>', delete, name='delete'),
    path('create/', create, name='create'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
]
