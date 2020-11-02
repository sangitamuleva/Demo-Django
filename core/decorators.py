from django.http import HttpResponse

def allowed_users(allowed_roles=[]):

    def decorator(view_fun):
        def wrapper_func(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                group = list(request.user.groups.values_list('name', flat=True))[0]  # QuerySet Object
   

            if group in allowed_roles:
                return view_fun(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized")
        return wrapper_func
    return decorator