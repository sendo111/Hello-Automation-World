from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'haw'
urlpatterns = [
    url('top/', views.top, name='top'),
    url('create/', views.create, name='create'),
    path('update/<int:book_id>', views.update, name='update'),
    path('delete/<int:book_id>', views.delete, name='delete'),
]
