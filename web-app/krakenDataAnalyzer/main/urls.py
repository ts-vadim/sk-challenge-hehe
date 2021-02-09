from django.urls import path
from .views import *


urlpatterns = [
	path('', homepage),
	path('rinfo/', request_info, name='rinfo'),
	path('tree/', project_tree, name='tree'),
	path('<path:url_path>/', path_download)
]