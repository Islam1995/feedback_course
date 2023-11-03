from django import forms 

from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label= "Your Name",
#                                 max_length=20,
                      
#                                 error_messages={
#                                     "required": "Your must entered your name!",
#                                     "max_length": "please entered short name!"
#                                 }
#     )
#     review_text = forms.CharField(label="Your Feedback",
#                                   widget= forms.Textarea,
#                                   max_length=200
#                                   )
#     rating = forms.IntegerField(label="Your Rating", max_value=5, min_value=1)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        #exculde = ['owner_comment']
        fields = "__all__"
        labels ={
            "user_name":"Your Name",
            "review_text": "Your Feedback",
            "rating":"Your Rating"
        } 
        error_messages= {
            "user_name":
                {
                    "required": "Your must entered your name!",
                    "max_length": "please entered short name!"
                }
        }
            