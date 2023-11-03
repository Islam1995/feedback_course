from django import forms 

class ReviewForm(forms.Form):
    user_name = forms.CharField(label= "Your Name",
                                max_length=20,
                      
                                error_messages={
                                    "required": "Your must entered your name!",
                                    "max_length": "please entered short name!"
                                }
    )
    