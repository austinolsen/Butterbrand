from django.conf.urls import url
from django.conf import settings
from . import views 
from django.conf.urls.static import static

app_name = 'main_app'

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^register/$', views.UserFormView.as_view(), name ='register'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
