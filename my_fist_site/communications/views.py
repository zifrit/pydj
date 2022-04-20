from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostFrom, CommentForm


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
    comments = post.comments.filter(active=True)

    new_comments = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comments = comment_form.save(commit=False)
            new_comments.post = post
            new_comments.save()


    else:
        comment_form = CommentForm()

    return render(request, 'commu/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comments': new_comments,
                   'comment_form': comment_form})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostFrom(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} рекомендоманвал к прочению {post.title}'
            massage = f'прочтите {post.title} по адресу {post_url}\n\n' \
                      f'{cd["name"]} коментарии : {cd["comments"]}'
            # sendemail
            sent = True

    else:
        form = EmailPostFrom
    return render(request, 'commu/share.html', {'post': post, 'form': form, 'sent': sent})

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
