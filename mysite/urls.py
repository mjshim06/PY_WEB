"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mysite.views import IndexView, aboutView, UserCreateView, UserCreateDoneTV

from bookmark.views import BookmarkLV, BookmarkDV, BookmarkCV, BookmarkUV, BookmarkRV
from blog.views import PostLV, PostDV, PostCV, PostUV, PostRV #추가

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$',aboutView.as_view(), name='about'),

    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^accounts/register/$',
        UserCreateView.as_view(),
        name='register'),

    url(r'^accounts/register/done/$',
        UserCreateDoneTV.as_view(),
        name='register_done'),

    url(r'^bookmark/$', BookmarkLV.as_view(),
        name='bookmark_index'),
    url(r'^bookmark/(?P<pk>\d+)/$',
        BookmarkDV.as_view(),
        name='detail'),

    url(r'^bookmark/add/$',
        BookmarkCV.as_view(),
        name='bookmark_create'),

    url(r'^bookmark/update/(?P<pk>[0-9]+)/$',
        BookmarkUV.as_view(),
        name='bookmark_update'),

    url(r'^bookmark/delete/(?P<pk>[0-9]+)/$',
        BookmarkRV.as_view(),
        name='bookmark_delete'),

    url(r'^blog/$', PostLV.as_view(),
        name='blog_index'),
    url(r'^blog/(?P<pk>\d+)/$',
        PostDV.as_view(),
        name='blog_detail'),

    url(r'^blog/add/$', PostCV.as_view(), name='post_create'), #추가
    url(r'^blog/update/(?P<pk>[0-9]+)/$', PostUV.as_view(), name='post_update'), #추가
    url(r'^blog/delete/(?P<pk>[0-9]+)/$', PostRV.as_view(), name='post_delete'), #추가

] + static(settings.MEDIA_URL,
           document_root= settings.MEDIA_ROOT)






































