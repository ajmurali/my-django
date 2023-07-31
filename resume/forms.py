from django import forms

class ProjectForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'formtitle'}))
    text = forms.CharField(label="Description", widget=forms.Textarea(attrs={'class': 'formtextarea'}))
    image = forms.FileField()
    sourcecode = forms.FileField()
    demo = forms.CharField(widget=forms.Textarea(attrs={'class': 'formdemo'}))