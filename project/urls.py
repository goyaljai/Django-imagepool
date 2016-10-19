from django.conf.urls import url

from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^follow/(?P<user_id>[0-9]+)/$', views.follow_user, name='follow'),
   #url(r'^login_user/$', 'django.contrib.auth.views.login',{'template_name': 'project/login.html','extra_context':{'next':'/imagepool/'}}, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'image/add/$', views.ImageCreate.as_view(), name='image-add'),
    url(r'^like_image/(?P<image_id>[0-9]+)/$', views.like_image, name='like-image'),
    url(r'all_users/$', views.UserListView.as_view(), name='all-users'),
    url(r'search/', views.search, name='search'),
    url(r'^login_user/$', views.LoginFormView.as_view(), name='login_user'),

    url(r'^unfollow/$', views.unfollow, name='unfollow'),
]
