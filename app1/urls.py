from . import views
from django.urls import path
from .views import robots_txt

urlpatterns = [
    path("", views.index, name="home"),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    path('contact', views.contact, name="contact"),
    path('gallery', views.gallery, name="gallery"),
    path('blog/<int:id>', views.blog, name="blog"),
    path('bloglist', views.bloglist, name="bloglist"),
    path('search', views.search, name="search"),
    path("robots.txt", robots_txt),
    # path('user', views.user, name="login"),
    # path('register', views.register, name="register"),
]
