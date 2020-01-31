from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('haw/', include('haw_book_manage.urls')),
]
