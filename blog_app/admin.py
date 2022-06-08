from django.contrib import admin

from blog_app.models import Blog, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','description']
    search_fields = ['name','email',]
    list_filter = ['email','name']
admin.site.register(Contact,ContactAdmin)    




# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['title','slug','text','status','published_at']
#     search_fields = ['title','text',]
#     list_filter = ['published_at',]
# admin.site.register(Blog,BlogAdmin)   

class ArticleAdmin(admin.ModelAdmin):
   prepopulated_fields = {
      "slug": ("title", )
   }


admin.site.register(Blog,ArticleAdmin)