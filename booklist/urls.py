from django.urls import path,include
from . import views

urlpatterns = [
    path('insert/', views.book_form, name = 'book_insert'),
    path('<int:id>/', views.book_form, name = 'book_update'),
    path('delete/<int:id>/', views.book_delete, name = 'book_delete'),
    path('',views.book_list, name = 'book_list')
]
