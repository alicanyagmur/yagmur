from django.shortcuts import render,get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.

def Landing_View(request):
    return render(request,'landing.html')



def Post_View(request):
    if request.user.is_authenticated():

        post_list = Post.objects.all()

        ##########  Search  ###########
        query = request.GET.get('q')
        if query:
            post_list = post_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)).distinct()
        ########## End Search ###########

        paginator = Paginator(post_list, 5)  # Show 5 contacts per page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request,'blog/blog.html',{'posts':posts})


    else:
        return render(request,'account/login.html')

def Post_Detail_View(request,slug):
    if request.user.is_authenticated():
        post = get_object_or_404(Post, slug=slug)

        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())

        context = {
            'post':post,
            'forn':form,
        }
        return render(request,'blog/detail.html',context)


    else:
        return render(request,'account/login.html')

def Post_Create_View(request):
    if request.user.is_authenticated():

        if request.user.is_superuser:

            form = PostForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request,'Başarılı bir şekilde oluşturdunuz.') # Trans edilecek
                return HttpResponseRedirect(post.get_absolute_url())



            context = {
                'form': form,
            }
            return render(request,'blog/create.html',context)

        else:
            posts = Post.objects.all()
            return render(request,'blog/blog.html',{'posts':posts})




    else:
        return render(request,'account/login.html')




def Post_Update_View(request,slug):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, slug=slug)
        if request.user.is_superuser:

            form = PostForm(request.POST or None, request.FILES or None, instance=post)

            if form.is_valid():
                form.save()
                messages.success(request, 'Başarılı bir şekilde güncellediniz.') # Trans edilecek
                return HttpResponseRedirect(post.get_absolute_url())

            context = {
                'form': form,
            }

            return render(request, 'blog/update.html', context)


        else:
            return HttpResponseRedirect(post.get_absolute_url())


    else:
        return render(request, 'account/login.html')


def Post_Delete_View(request, slug):
    if request.user.is_authenticated():
        post = get_object_or_404(Post, slug=slug)
        if request.user.is_superuser:
            post.delete()
            messages.warning(request, 'Başarılı bir şekilde sildiniz.') # Trans edilecek
            return redirect('post:blog')

        else:
            return HttpResponseRedirect(post.get_absolute_url())

    else:
        return render(request, 'account/login.html')