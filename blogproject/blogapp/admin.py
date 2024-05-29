from django.contrib import admin
from blogapp.models import Post,Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    list_filter = ['author','title']
    # raw_id_fields = ('author',)
    search_fields = ('title','body','status')
    prepopulated_fields = {'slug':('title',)}

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','body','active','created','updated']
    list_filter = ['active','created','updated']
    # raw_id_fields = ('author',)
    search_fields = ('name','email','body')
    # prepopulated_fields = {'slug':('title',)}

admin.site.register(Post,PostAdmin)
admin.site.register(Comments,CommentsAdmin)

