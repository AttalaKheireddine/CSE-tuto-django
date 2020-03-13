from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index_view(request):

    articles = Article.objects.all()
    our_context = {"articles" : articles}
    return render(request, "index_template.html",our_context)