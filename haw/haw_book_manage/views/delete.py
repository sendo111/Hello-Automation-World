from django.contrib import messages
from django.shortcuts import redirect
from ..models import TblBook


def delete(request, book_id):
    tb = TblBook.objects.get(id=book_id)

    try:
        tb.delete()
    except Exception:
        messages.error(request, f'更新に失敗しました')
        redirect('/haw/top')

    return redirect('/haw/top')
