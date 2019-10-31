from django.http import HttpResponse

def index(request):
    return HttpResponse('A list of ads will be displayed here.')
