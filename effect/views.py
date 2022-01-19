from django.shortcuts import render

# Create your views here.
from effect.models import Effect


def index(request):
    # verbs = Verb.objects.all()
    return render(request, 'effect/search.html')


def reg(request):
    if request.method == "POST":
        kr = request.POST['kr']
        jp = request.POST['jp']
        jp_hi = request.POST['jp_hi']
        author = request.POST['author']
        num = request.POST['num']
        title = request.POST['title']
        pages = request.POST['pages']
        verb = Verb(kr=kr, jp=jp, jp_hi=jp_hi, author=author, num=num, title=title, pages=pages)
        verb.save()
        return HttpResponseRedirect('/reg/list/')
    else:
        return render(request, 'effect/reg.html')
