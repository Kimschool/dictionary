from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from verb.models import Verb

def index(request):
    verbs = {'verbs': Verb.objects.all()}
    return render(request, 'verb/list.html', verbs)

def search(request):
    if request.method == "POST":
        word = request.POST['word']
        if word != '':
            verbs = Verb.objects.filter(kr__contains=word)
            counts = Verb.objects.filter(kr__contains=word).count()
        else:
            verbs = Verb.objects.all()
            counts = Verb.objects.all().count()

        # return render(request, 'verb/list.html', verbs)
        return render(request, 'verb/list.html', {'verbs': verbs, 'counts': counts})
    else:
        return render(request, 'verb/search.html')

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
        return HttpResponseRedirect('/verb/list/')
    else:
        return render(request, 'verb/reg.html')
