from django.shortcuts import render, redirect
from django.utils import timezone
from ..models import TblBook


def create(request):
    template_name = 'create.html'

    if not request.POST:
        return render(request, template_name)
    else:
        tb = TblBook(
            title=request.POST['title'],
            author=request.POST['author'],
            publisher=request.POST['publisher'],
            finished_date=request.POST['finished_date'],
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        tb.save()

        return redirect('/haw/top')
