from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError as Http500
import os


# Create your views here.
def homepage(request):
	return HttpResponse(
		'''
		<h1>Homepage</h1><br>
		Try <a href="rinfo/">request info</a><br>
		<a href="admin/">Admin</a><br>
		<a href="tree/">Project tree</a><br>
		'''
	)


def path_download(request, path: str):
	cwd = os.getcwd()
	ospath = os.path.join(cwd, path)
	if os.path.exists(ospath):
		if os.path.isdir(ospath):
			return HttpResponse('\"' + path + '\" is a directory')
		with open(ospath, 'rb') as file:
			response = HttpResponse(file.read(), content_type="application/force-download")
			response['Content-Disposition'] = 'inline; filename=' + path.split('/')[-1]
			return response
	return HttpResponse('File \"' + path + '\" not found')
	


def request_info(request):
	response = ''
	try:
		response += '''<b>WSGIRequest summary:</b><br>
	<b>Path:</b> <small>{0}</small><br>
	<b>Path info:</b> <small>{1}</small><br>
	<b>Method:</b> <small>{3}</small><br>
	<b>Environment:</b><br>
		{2}<br>
	'''.format(
		str(request.path),
		str(request.path_info),
		'<br>\t'.join([key + ': <small>' + str(request.environ[key]) + '</small>' for key in request.environ.keys()]),
		str(request.method)
	)
	except Exception as e:
		response = '<br>Exception:</b> ' + str(e)
	
	header = "<h1><a href=\"/\">Homepage</a></h1><br>"
	return HttpResponse(header + response)


def project_tree(request):
	tree = dict()
	start_dir = os.getcwd()
	for path in os.walk(start_dir):
		cwd = path[0]
		dirs = path[1]
		files = path[2]
		tree[cwd.replace(start_dir, '')] = (dirs, files)
	
	response = "<h1><a href=\"/\">Homepage</a></h1><br>"
	for key, value in tree.items():
		for files in value:
			for file in files:
				p = os.path.join(key, file)
				response += '<a href=\"' + p + '\">' + p + '</a><br>'
	return HttpResponse(response)
