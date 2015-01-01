from django.conf.urls import patterns, include, url
# from django.conf.urls.defaults import *
from django.conf.urls import *
from dbe.blog.models import *
from dbe.blog.views import PostView, Main, ArchiveMonth

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dbe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns("dbe.blog.views",
   (r"^post/(?P<dpk>\d+)/$"          , PostView.as_view(), {}, "post"),
   (r"^archive_month/(\d+)/(\d+)/$"  , ArchiveMonth.as_view(), {}, "archive_month"),
   (r"^$"                            , Main.as_view(), {}, "main"),
   # (r"^delete_comment/(\d+)/$"       , "delete_comment", {}, "delete_comment"),
)

