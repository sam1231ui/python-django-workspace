from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def show(request):
    return HttpResponse("This is polls 2nd page or view for same polls folder")
