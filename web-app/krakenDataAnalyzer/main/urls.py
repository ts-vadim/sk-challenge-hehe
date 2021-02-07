from django.urls import path
from .views import *


urlpatterns = [
	path('', homepage, name='home'),
	path('rinfo/', request_info, name='rinfo'),
	path('tree/', project_tree, name='tree'),
	path('<path:path>/', path_download)
]