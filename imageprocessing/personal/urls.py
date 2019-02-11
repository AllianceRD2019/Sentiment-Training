from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
url(r'^$', views.home, name='home'),

#environment
url(r'^add_env', views.add_env, name='add_env'),

#config

#document
url(r'^add_document', views.add_document, name='add_document'),
url(r'^get_document', views.get_document, name='get_document'),
url(r'^update_document', views.update_document, name='update_document'),
url(r'^delete_document', views.delete_document, name='delete_document'),


#collection
url(r'^add_collection', views.add_collection, name='add_collection'),
url(r'^list_collection', views.list_collection, name='list_collection'),
url(r'^update_collection', views.update_collection, name='update_collection'),


#nlu
url(r'^nlu', views.nlu, name='nlu'),
url(r'^dataset/', views.dataset, name='dataset'),\
url(r'^interface/', views.interface, name='interface'),
url(r'^charts/', views.charts, name='charts'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)