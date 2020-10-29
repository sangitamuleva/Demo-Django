from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Registration Completed for {username}")
            
            return redirect('login')

    form=UserCreationForm()
    context={'form':form}
    return render(request,'auth/register.html',context)

def login(request):
    context={}
    return render(request,'auth/login.html',context)

@login_required
def home(request):
    return render(request,'post/all_post.html',context)
