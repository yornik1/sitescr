from django.conf.urls import url
from .views import index, top

urlpatterns = [
    url(r'^$', index),
    url(r'^top/(?P<name>[A-Za-z0-9]+)/$', top),

]
