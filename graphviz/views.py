from django.http import HttpResponse

def dot_file(request, slug, template='graphviz/dot_file.html'):
    return HttpResponse('todo')

def image_file(request, slug, template='graphviz/dot_file.html'):
    return HttpResponse('todo image')