from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse("<h1>Hello World!</h1>")