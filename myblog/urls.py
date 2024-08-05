"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from blog.sitemaps import PostSitemap
from blog.views import homepage # import the homepage view

# Define sitemap dictionary. This dictionary maps the name 'posts' to the PostSitemap class. 
#It’s used by the sitemap view to generate the XML for different sitemaps.
sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls), # Routes requests for /admin/ to the Django admin interface
    path('blog/', include('blog.urls', namespace='blog')), # Routes requests for /blog/ to the URLs defined in the blog application
    path(
        'sitemap.xml', #  the URL pattern that the  application will match for sitemap requests
        sitemap, # sitemap view
        {'sitemaps': sitemaps}, # dictitonary of parameters passed to the view
        name='django.contrib.sitemaps.views.sitemap' # name of the URL pattern
    )
]
