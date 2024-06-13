from django.urls import path 
from . import views

urlpatterns = [
    path('get-books', views.get_books, name='get-books'),
    path('borrow-a-book/<int:pk>', views.borrow_book),
    path("", views.test_token),
    path("stars/<int:pk>", views.stars),
    path('comments/<int:pk>', views.comment)
]