from django.urls import path
from .views import *


urlpatterns = [
	path('', homepage),
	path('rinfo/', request_info),
	path('tree/', project_tree),
	path('<path:path>/', path_download)
]