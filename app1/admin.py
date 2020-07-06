from django.contrib import admin

from .models import Subscribe, myblog, Contact,Gallery
# Register your models here.


class subscribeView(admin.ModelAdmin):
    list_display = ('id','email')

class galleryView(admin.ModelAdmin):
    list_display = ('image_id','image', 'date')

class blogView(admin.ModelAdmin):
    list_display = ('blog_id', 'blog_title', 'pub_date')


class contactView(admin.ModelAdmin):
    list_display = ('id', 'personname', 'email', 'subject')


admin.site.register(Subscribe,subscribeView)
admin.site.register(myblog,blogView)
admin.site.register(Contact,contactView)
admin.site.register(Gallery,galleryView)

admin.site.site_header = "Zakria Official Blog"
