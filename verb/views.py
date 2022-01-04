from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from verb.models import Verb

def index(request):
    verbs = {'verbs': Verb.objects.all()}
    return render(request, 'verb/list.html', verbs)

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
        return HttpResponseRedirect('/')
    else:
        return render(request, 'verb/reg.html')
