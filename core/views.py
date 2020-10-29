from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required

from .models import Post
# Create your views here.

# class post_list(DetailView):
#     model= Post

class post_create(CreateView):
    model= Post
    fields=['title','content']
    template_name='post/create_post.html'

class post_list(ListView):
    model = Post
    template_name='post/all_post.html'

class post_detail(DetailView):
    model= Post
    template_name='post/post_detail.html'

class post_update(UpdateView):
    model= Post
    template_name='post/update_post.html'
    fields=['title','content']
    success_url='/'

class post_delete(DeleteView):
    model= Post
    template_name='post/post_confirm_delete.html'    
    success_url='/'

@login_required
def list_view(request): 
   
    context ={} 
  
    context["posts"] = Post.objects.all() 
          
    return render(request, "list_view.html", context) 