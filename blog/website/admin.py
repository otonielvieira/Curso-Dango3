from django.contrib import admin
from .models import Posts

class PostAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'sub_title', 'content', 'categories', 'deleted']
    search_fields = ['id','title', 'sub_title', 'content']

    def get_queryset(self, request):
        return Posts.objects.filter(deleted=True)


# Register your models here.
admin.site.register(Posts, PostAdmin)
