from django.http import HttpResponse

def home(request):
    return HttpResponse('<html><title>To-Do Lists</title></html>')

