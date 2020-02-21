from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^searchbusiness/', views.search_neighborhood, name='search_neighborhood'),
    url(r'^searchlocation',views.search_business, name="search_business"),
    url(r'business/(\d+)', views.single_business,name='singlebusiness'),
    url(r'news/(\d+)', views.single_news,name="singlenews"),
    url(r'profile/(?P<userid>\d+)',views.single_profile,name='singleprofile'),
    url(r'create/profile$', views.createprofile,name='createprofile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)