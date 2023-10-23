from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    if request.method == "POST":
        entered_name = request.POST["username"]
        print(entered_name)
        return HttpResponseRedirect("/thank-you")
    
    return render(request, "reviews/reviews.html")


def thank_you(request):
    return render(request, "reviews/thank_you.html")
