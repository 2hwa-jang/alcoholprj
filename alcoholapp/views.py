from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.

def home(request):
    return render(request, 'home.html')

def list_of_post_by_category(request):
    categories = Category.objects.all()
    post = Post.objects
    #if category_slug:
        #category = get_object_or_404(Category, slug=category_slug)
        #post = post.filter(category=category)
    template = 'list_of_post_by_category.html'
    context = {'categories' : categories, 'post' : post, 'category' : category}
    return render(request, template, context)

def icecream(request):
    posts = Post.objects
    return render(request, 'icecream.html', {'posts':posts})

def beverage(request):
    posts = Post.objects
    return render(request, 'beverage.html', {'posts':posts})

def others(request):
    posts = Post.objects
    return render(request, 'others.html', {'posts':posts})

def new(request):
    return render(request, 'new.html')
