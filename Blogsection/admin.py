from django.contrib import admin
from Blogsection.models import popular
from Blogsection.models import latest
from Blogsection.models import trending
from Blogsection.models import aboutus
from Blogsection.models import allblogs


# Register your models here.

class blogAdmin(admin.ModelAdmin):
    list_display=('blog_title2','blog_desc1','blog_title','blog_img','blog_desc')

admin.site.register(popular,blogAdmin)


class blogAdmin(admin.ModelAdmin):
    list_display=('blog_title2','blog_desc','blog_title','blog_img')

admin.site.register(latest,blogAdmin)

class blogAdmin(admin.ModelAdmin):
    list_display=('blog_title2','blog_desc','blog_img','blog_title')

admin.site.register(trending,blogAdmin)

class blogAdmin(admin.ModelAdmin):
    list_display=('blog_title1','blog_img1','blog_desc1','blog_desc2','blog_desc3','blog_title2','blog_img2')

admin.site.register(aboutus,blogAdmin)


class blogAdmin(admin.ModelAdmin):
    list_display=('blog_title','blog_img')

admin.site.register(allblogs,blogAdmin)

