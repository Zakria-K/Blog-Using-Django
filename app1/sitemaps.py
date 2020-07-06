from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import myblog
import datetime


class StaticViewSitemap(Sitemap):

    def items(self):
        return['home','about','contact','projects','gallery','bloglist']
    
    def location(self, item):
        return reverse(item)