from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
#from .models import Review
# Create your views here.

def index(request):
    
    if request.method == "POST":
    #    entered_name = request.POST["username"]
        form = ReviewForm(request.POST)
    #    if entered_name == "" and len(entered_name) >= 100:
    #        return render(request, "reviews/reviews.html",{
    #            "has_error": True           })
        if form.is_valid():
            form.save()
            # review = Review(user_name= form.cleaned_data['user_name'],
            #                 review_text= form.cleaned_data['review_text'],
            #                 rating= form.cleaned_data['rating'])
            #review.save()
            #print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, "reviews/reviews.html",{
                "form": form
            })

def thank_you(request):
    return render(request, "reviews/thank_you.html")
# print(entered_name)
