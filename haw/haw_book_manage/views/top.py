from django.shortcuts import render
from ..models import TblBook


def top(request):
    template_name = 'top.html'
    book_list = list(TblBook.objects.all().values())
    books = {'books': book_list}

    return render(request, template_name, books)
