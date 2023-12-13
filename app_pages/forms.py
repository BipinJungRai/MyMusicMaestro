from django import forms


# RecommendFriendForm is a Django Form class that is used to create a form for recommending a friend
class RecommendFriendForm(forms.Form):
    to = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
