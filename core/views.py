from django.http import HttpResponse

def index(request):
    return HttpResponse('''
        <div>
            <h1 style="color:black;text-align:center;margin:30px;font-size:24px">
                <span style="text-shadow:1px 1px lightgray">
                    Abdulwahab's Stackoverflow API is working ...
                </span>
            </h1>
        </div>
    ''')