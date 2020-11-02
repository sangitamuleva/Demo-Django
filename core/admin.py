from django.contrib import admin
from django.contrib.auth.models import User,Group
# Register your models here.


from core.models import *

admin.site.site_header='Custom Admin'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','updated_on')
    # list_filter=('created_on',)

# admin.site.unregister(Group)
# admin.site.unregister(User)
admin.site.register(Category)
admin.site.register(SubCategory)