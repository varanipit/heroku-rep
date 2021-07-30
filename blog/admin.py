from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = [
        'title',
        'date_created',
        'date_updated'
    ]
admin.site.register(Post, PostAdmin)
