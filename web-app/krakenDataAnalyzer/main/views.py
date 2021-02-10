from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError as Http500
from main.models import SiteMember
import os



def homepage(request):
	return render(request, 'main/home.html', {'members': SiteMember.objects.all()})


def path_download(request, url_path: str):
	url_path = url_path.replace('"', '')
	cwd = os.getcwd()
	# WTF
	ospath = cwd + os.path.sep + url_path.replace('/', os.path.sep)
	ospath = ospath.replace(os.path.sep * 2, os.path.sep)

	if os.path.exists(ospath) and not os.path.isdir(ospath):
		with open(ospath, 'rb') as file:
			response = HttpResponse(file.read(), content_type="text/plain")# application/force-download
			response['Content-Disposition'] = 'inline; filename=' + url_path.split('/')[-1]
			return response
	return HttpResponse('File \"' + url_path + '\" not found')


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
	hidden_list = [
		'__pycache__',
		'__init__.py',
		'migrations'
	]

	tree = dict()
	start_dir = os.getcwd()
	files_to_render = list()

	for path in os.walk(start_dir):
		cwd = path[0]
		dirs = path[1]
		files = path[2]
		if cwd.split(os.path.sep)[-1] in hidden_list:
			continue
		for file in files:
			if file in hidden_list:
				continue
			filepath = os.path.join(cwd.replace(start_dir, ''), file)
			files_to_render.append((filepath, '/' + filepath))
	
	return render(request, 'main/tree.html', {'files': files_to_render})
