
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from project import views
from allauth.account import views as jai

urlpatterns = [
    url(r'^', include('project.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login_user/$', views.TheLoginView.as_view(),
        kwargs={'redirect_authenticated_user': True}, name='login_user'),
    url(r'^login/$', jai.LoginView.as_view(),
        kwargs={'redirect_authenticated_user': True}, name='login'),
    url(r'^', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)