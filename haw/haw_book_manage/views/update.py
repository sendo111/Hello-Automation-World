from django.shortcuts import render, redirect
from django.utils import timezone
from ..models import TblBook


def update(request, book_id):
    template_name = 'update.html'

    if len(request.POST) == 1:
        bt = TblBook.objects.values(
            'id',
            'title',
            'author',
            'publisher',
            'finished_date'
        ).get(id=book_id)
        return render(request, template_name, bt)
    else:
        update_bt = TblBook.objects.get(id=book_id)
        update_bt.title = request.POST['title']
        update_bt.author = request.POST['author']
        update_bt.publisher = request.POST['publisher']
        update_bt.finished_date = request.POST['finished_date']
        update_bt.updated_at = timezone.now()
        update_bt.save()

        return redirect('/haw/top')
