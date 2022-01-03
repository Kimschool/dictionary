from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'board/list.html')

def post(request):
    return render(request, 'board/post.html')