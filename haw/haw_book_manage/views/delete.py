from django.shortcuts import render, redirect
from ..models import TblBook


def delete(request, book_id):
    tb = TblBook.objects.get(id=book_id)
    tb.delete()

    return redirect('/haw/top')
