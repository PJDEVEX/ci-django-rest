"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # login and logout views for the browsable API
    # https://www.django-rest-framework.org/
    path('api-auth/', include('rest_framework.urls')),
    # dj_rest_auth urls
    #  https://dj-rest-auth.readthedocs.io/en/latest/installation.html 
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # Adding profiles.urls in the main router
    path('', include('app_profile.urls')),
    # Adding posts.url in the main router
    path('', include('posts.urls')),
    # Adding comments.urls 
    path('', include('comments.urls')),
    # Adding likes.urls
    path('', include('likes.urls')),
    path('', include('followers.urls'))
]
