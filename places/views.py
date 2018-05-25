from django.http import HttpResponse
from django.shortcuts import render
from inf25.tasks import generate_file
# Create your views here.
def post_list(request):
    generate_file()
    return HttpResponse("You're looking at question %s." % 123)