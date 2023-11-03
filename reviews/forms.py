from django import forms 

class ReviewForm(forms.Form):
    user_name = forms.CharField(label= "Your Name",
                                max_length=20,
                      
                                error_messages={
                                    "required": "Your must entered your name!",
                                    "max_length": "please entered short name!"
                                }
    )
    review_text = forms.CharField(label="Your Feedback",
                                  widget= forms.Textarea,
                                  max_length=200
                                  )
    rating = forms.IntegerField(label="Your Rating", max_value=5, min_value=1)
    