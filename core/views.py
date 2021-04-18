from django.http import HttpResponse

def index(request):
    return HttpResponse("Abdulwahab's Stackoverflow API is working ...")