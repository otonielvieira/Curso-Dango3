from django.contrib import admin
from .models import Posts
from .models import Contato

class PostAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'sub_title', 'content', 'categories', 'deleted']
    search_fields = ['id','title', 'sub_title', 'content']

    def get_queryset(self, request):
        return Posts.objects.filter(deleted=True)


# Register your models here.
admin.site.register(Posts, PostAdmin)
admin.site.register(Contato)
