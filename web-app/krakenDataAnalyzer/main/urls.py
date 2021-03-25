from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('', homepage),
	path('rinfo/', request_info, name='rinfo'),
	path('tree/', project_tree, name='tree'),
	path('upload/', upload, name='upload'),
	path('<path:url_path>/', path_download)
]