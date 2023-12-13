from django import forms


class RecommendFriendForm(forms.Form):
    to = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
