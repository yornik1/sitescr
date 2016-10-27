from django import forms


class InstaName(forms.Form):
    name = forms.CharField(max_length=64, required=True)
    top_count = forms.IntegerField(min_value=0, required=False)
    videos = forms.BooleanField(required=False)


class RemoveInstaName(forms.Form):
    name_del = forms.CharField(max_length=64, required=True)
