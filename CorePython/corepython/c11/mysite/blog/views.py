from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from models import BlogPost


# Create your views here.
# RequestContext to handle CSRF token
def archive(request):
    posts = BlogPost.objects.all()[:10]
    return render(request, 'archive.html', {'posts': posts})


def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=datetime.now()
        ).save()
    return HttpResponseRedirect('/blog/')
