from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def list_coom(request):
    objects_list = Post.objects.all()
    paginator = Paginator(objects_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'commu/list.html', {'posts': posts, 'page': page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'commu/detail.html',
                  {'post': post})

# def communications_list(request, *args, **kwargs):
#     return render(request, 'commu/commun_ht.html', {})
#
#
# def com_list(request, *args, **kwargs):
#     return render(request, 'commu/content.html', {})
#
#
# class CVg(View):
#     def get(self, request):
#         return render(request, 'commu/register.html')
