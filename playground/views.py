from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World!")

def home(request):
    people = [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25},
        {"name": "Doe", "age": 22}
    ]
    return render(request, 'tables.html', {'people': people})

def google_redirect(request):
    return render(request, 'indexes.html', {'name' : 'Sarank'})