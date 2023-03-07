from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemap import BlogSitemap, CategorySitemap
from .views import IndexView, BlogDetailView, AuthorView

app_name = 'blog'

sitemaps = {
    'blog':BlogSitemap,
    'category':CategorySitemap
}

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('story/<slug:slug>/',BlogDetailView.as_view(), name='blog-detail'),
    path('author/',AuthorView.as_view(), name='author'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]