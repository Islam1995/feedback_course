from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
# Create your views here.

def index(request):
    
    if request.method == "POST":
    #    entered_name = request.POST["username"]
        form = ReviewForm(request.POST)
    #    if entered_name == "" and len(entered_name) >= 100:
    #        return render(request, "reviews/reviews.html",{
    #            "has_error": True           })
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, "reviews/reviews.html",{
                "form": form
            })

def thank_you(request):
    return render(request, "reviews/thank_you.html")
# print(entered_name)
