from django.http import HttpResponse

def index(request):
    return HttpResponse("Abdulwahab's stackoverflow API is working ...")