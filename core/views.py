from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

from .models import Post

# Create your views here.


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

# @login_required
# def list_view(request): 
   
#     context ={}   
#     context["posts"] = Post.objects.all()           
#     return render(request, "list_view.html", context) 


# Function based view

def category_create(request):
    
    if request.method == 'POST':
        form=CategoryForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() 
            return redirect('all_category')
    else:
        form=CategoryForm()

    context={'form':form}

    return render(request,'category/create_category.html',context)


def category_list(request):
    category=Category.objects.all()
    context={'category':category}

    return render(request,'category/all_category.html',context)

def category_detail(request,pk):
    category=Category.objects.get(id=pk)
    context={'category':category}

    return render(request,'category/category_detail.html',context)
    
def category_update(request,pk):
    category=get_object_or_404(Category,id=pk)

    if request.method == 'POST':
        form=CategoryForm(request.POST, request.FILES,instance=category)
        if form.is_valid(): 
            edit=form.save(commit=False) 
            edit.save()
            return redirect('all_category')
    else:
        form=CategoryForm(instance=category)
    context={'form':form}
    return render(request,'category/update_category.html',context)

def category_delete(request,pk):
    category=get_object_or_404(Category,id=pk)

    if request.method=='POST':
        category.delete()
        return redirect('all_category')
    return render(request,'category/category_confirm_delete.html')

# Sub Category

def subcategory_create(request):
    
    if request.method == 'POST':
        form=SubCategoryForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() 
            return redirect('all_subcategory')
    else:
        form=SubCategoryForm()

    context={'form':form}

    return render(request,'subcategory/create_subcategory.html',context)


def subcategory_list(request):
    subcategory=SubCategory.objects.all()
    context={'subcategory':subcategory}

    return render(request,'subcategory/all_subcategory.html',context)

def subcategory_detail(request,pk):
    subcategory=SubCategory.objects.get(id=pk)
    context={'subcategory':subcategory}

    return render(request,'subcategory/subcategory_detail.html',context)
    
def subcategory_update(request,pk):
    subcategory=get_object_or_404(SubCategory,id=pk)

    if request.method == 'POST':
        form=SubCategoryForm(request.POST, request.FILES,instance=subcategory)
        if form.is_valid(): 
            edit=form.save(commit=False) 
            edit.save()
            return redirect('all_subcategory')
    else:
        form=SubCategoryForm(instance=subcategory)
    context={'form':form}
    return render(request,'subcategory/update_subcategory.html',context)

def subcategory_delete(request,pk):
    subcategory=get_object_or_404(SubCategory,id=pk)

    if request.method=='POST':
        subcategory.delete()
        return redirect('all_subcategory')
    return render(request,'subcategory/subcategory_confirm_delete.html')