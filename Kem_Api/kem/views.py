from django.http import HttpResponse
from django.http import JsonResponse
from ..kem import KemMongoCache


def test(request):
    keyword = request.GET['keyword']
    num = request.GET['num']
    kemObject = KemMongoCache('mongodb://140.120.13.243:4444/')
    
    
    return JsonResponse(kemObject.getTerms(keyword, int(num)), safe = False)


    # return HttpResponse("<h1>Hello World!</h1>")